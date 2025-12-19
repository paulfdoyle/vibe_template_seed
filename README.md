# Vibe Template

A neutral, SRMS-free starter repo that packages the delivery process (personas, stage actions, DoD), sample project, optional BugMgmt module, and a basic UI report template. Use this as a seed when creating new AI/VIBE-style projects.

## What you get
- Standard process docs and personas in `DOCS/`.
- Sample project scaffolding in `DOCS/projects/sample_project/`.
- Optional BugMgmt module: `scripts/issues.py`, `issues/` store, exports in `json-data/`, UI in `UI/` with bundled assets.
- Basic UI report template in `UI/templates/report_base.html` with bundled CSS/JS.

## Quickstart
1) Open a shell at the template root (`vibe_template_seed/`). Create a venv (optional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2) Regenerate BugMgmt exports from the sample data (run from the template root so paths stay local; otherwise pass `--data vibe_template_seed/issues/issues.jsonl`):
   ```bash
   python scripts/issues.py list --format json --output json-data/bugmgmt_issues.json
   python scripts/issues.py list --format html --output UI/bugmgmt_issues.html
   ```
3) Open `UI/bugmgmt_issues.html` via `file://` to view the sample issues.
4) Read the process in `DOCS/process.md` and the sample project plan in `DOCS/projectplan.md`.
5) For full adoption steps, see `DOCS/template_howto.md`. Before sharing, walk through `DOCS/template_release_checklist.md`.
6) If you haven’t renamed the project yet, start with the Project Creator/Owner persona in `DOCS/process.md` to set the project name/purpose and update `DOCS/projectplan.md` and project paths.

## Optional modules
- BugMgmt: keep if you want local issue tracking; remove or ignore `issues/`, `json-data/`, `UI/bugmgmt_issues.html`, and `scripts/issues.py` if not needed.
- UI template: extend `UI/templates/report_base.html` for lightweight static reports.
- LaTeX user docs: start from `DOCS/user_docs/user_doc_template.tex` if you want PDF user guides.

## Notes
- Sample data is PII-free and deterministic.
- All assets are local; no external network calls are required.
- Update paths via CLI flags or env vars (see `python scripts/issues.py --help`).
