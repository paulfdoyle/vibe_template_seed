#!/usr/bin/env python3
"""Lightweight local issue tracker helper (template version).

Reads a JSONL issue store and produces JSON or HTML exports with deterministic ordering.
All paths are configurable via flags; defaults assume running from the template root.
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any

SEVERITY_ORDER = ["critical", "major", "minor", "nit"]
STATUS_ORDER = ["open", "in_progress", "closed"]


def _load_issues(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _severity_weight(severity: str) -> int:
    try:
        return SEVERITY_ORDER.index(severity.lower())
    except ValueError:
        return len(SEVERITY_ORDER)


def _status_weight(status: str) -> int:
    try:
        return STATUS_ORDER.index(status.lower())
    except ValueError:
        return len(STATUS_ORDER)


def _norm(val: Any) -> str:
    return "" if val is None else str(val).strip()


def _sorted(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        rows,
        key=lambda r: (
            _status_weight(_norm(r.get("status", ""))),
            _norm(r.get("project", "")).lower(),
            _severity_weight(_norm(r.get("severity", ""))),
            _norm(r.get("id", "")),
        ),
    )


def _to_json(rows: List[Dict[str, Any]]) -> str:
    return json.dumps(rows, ensure_ascii=True, separators=(",", ":"))


def _to_html(rows: List[Dict[str, Any]], json_rel_path: Path) -> str:
    data_json = json.dumps(rows, ensure_ascii=True)
    json_path_str = json_rel_path.as_posix()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>BugMgmt Issues</title>
  <link rel="stylesheet" href="assets/bugmgmt.css" />
</head>
<body>
  <div class="container">
    <div class="hero">
      <div>
        <h1 class="h4">BugMgmt Issues</h1>
        <p class="muted small">Local, PII-free issues · Deterministic sort (status → project → severity → ID)</p>
      </div>
      <div class="badges">
        <span class="chip" id="totalCount"></span>
      </div>
    </div>

    <div class="card filters">
      <div class="filter-grid">
        <label>Project<select id="project"></select></label>
        <label>Status<select id="status"></select></label>
        <label>Severity<select id="severity"></select></label>
        <label>Phase<select id="phase"></select></label>
        <label>Stage<select id="stage"></select></label>
        <label>Search<input id="search" placeholder="Search text..." /></label>
        <button id="resetFilters" class="btn">Reset filters</button>
      </div>
      <div class="filter-hint">Source: issues/issues.jsonl · Regenerate via <code>python scripts/issues.py list --format html --output UI/bugmgmt_issues.html</code></div>
    </div>

    <div class="summary" id="summaryRow"></div>

    <div class="card">
      <div class="table-wrap">
        <table class="issues">
          <thead>
            <tr>
              <th>ID</th><th>Status</th><th>Severity</th><th>Project</th><th>Phase</th><th>Stage</th><th>Area</th><th>Details</th>
            </tr>
          </thead>
          <tbody id="issues-body"></tbody>
        </table>
      </div>
    </div>
    <p class="footer muted">Open locally via file://; uses local assets with inline fallback data.</p>
  </div>
  <script>
    window.BUGMGMT_CONFIG = {{ jsonPath: "{json_path_str}" }};
    window.BUGMGMT_FALLBACK = {data_json};
  </script>
  <script src="assets/bugmgmt.js"></script>
</body>
</html>
"""


@dataclass
class Paths:
    data: Path
    json_out: Path
    html_out: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local issue tracker helper (template)")
    parser.add_argument("command", choices=["list"], help="Command to run")
    parser.add_argument("--data", type=Path, default=Path("issues/issues.jsonl"), help="Path to JSONL store")
    parser.add_argument("--format", choices=["json", "html"], default="json", help="Output format")
    parser.add_argument("--output", type=Path, default=None, help="Output file path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _sorted(_load_issues(args.data))
    if args.format == "json":
        content = _to_json(rows)
        default_out = Path("json-data/bugmgmt_issues.json")
    else:
        # derive relative JSON path for the UI to fetch (defaults assume UI/ alongside json-data/)
        default_out = Path("UI/bugmgmt_issues.html")
        json_path = Path("json-data/bugmgmt_issues.json")
        html_out = Path(args.output) if args.output else default_out
        # compute relative path from HTML dir to JSON file
        rel_json = Path(os.path.relpath(json_path, start=html_out.parent))
        content = _to_html(rows, rel_json)
    out_path = args.output or default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
