# Repository Guidelines

## Project Structure & Module Organization
This repository is a documentation-first template with a lightweight local issue tracker. Core paths:
- `support/`: process docs, templates, BugMgmt tooling, and UI reports/styles (`support/docs/`, `support/ui/`, `support/scripts/`).
- `projects/`: project planning docs (one directory per project).
- Workspace directories for product work: `src/`, `tests/`, `config/`, `data/`, `assets/`, `scripts/`, `docs/`.
- BugMgmt source of truth: `support/bugmgmt/issues/issues.jsonl`; exports under `support/bugmgmt/exports/json/` and `support/ui/bugmgmt_issues.html`.

## Build, Test, and Development Commands
Run commands from the repo root so relative paths resolve. Use `python` if it maps to Python 3; verify with `python3 --version` or `python --version`.
- `python3 -m venv .venv` and `source .venv/bin/activate`: optional local virtualenv.
- `python3 support/scripts/issues.py list --format json --output support/bugmgmt/exports/json/bugmgmt_issues.json`: regenerate JSON export.
- `python3 support/scripts/issues.py list --format html --output support/ui/bugmgmt_issues.html`: regenerate HTML report.
- `python3 support/scripts/init_project.py --project <project> --prefix <PREFIX> --owner "Name"`: scaffold a new project and update the project plan.
- `python3 support/scripts/render_docs.py`: render `support/docs/` and `projects/` to `support/ui/docs/`.
- `python3 support/scripts/watch_docs.py`: auto-render `support/ui/docs/` when markdown changes.
- `pdflatex process_guide.tex`: build the process guide PDF from `support/docs/user_docs/`.
- Open `support/ui/bugmgmt_issues.html` via `file://` to view locally rendered issues.
- After any bug update, recreate the HTML report (and JSON export) so the UI stays in sync.

## Coding Style & Naming Conventions
- Python uses 4-space indentation, type hints, and `snake_case` for functions/variables.
- Issue fields are lowercase keys (`status`, `severity`, `project`, etc.). Use status values `open`, `in_progress`, `closed` and severity values `critical`, `major`, `minor`, `nit` to preserve deterministic ordering. For new bugs, include detail fields `root_cause`, `proposed_fix`, `qa_reproduction`. `owner` defaults from `BUGMGMT_REPO_OWNER` or `git config user.name`, with optional overrides in `PROJECT_OWNERS`, when set to `unassigned`.
- Example JSONL entry (single line):
  ```json
  {"id":"BMG-2025-01-003","date":"2025-01-07","project":"bugmgmt","phase":"01","stage":"foundation","area":"docs","status":"open","severity":"minor","summary":"Short description","owner":"unassigned","root_cause":"TBD","proposed_fix":"TBD","qa_reproduction":"TBD"}
  ```
- Issue IDs follow the project prefix pattern (example: `BMG-2025-01-001`). Update prefixes in `support/scripts/issues.py` (`PROJECT_PREFIXES`, e.g., `BMG`, `PMG`) when adding projects.
- Prefer `snake_case` for filenames (matches `bugmgmt_issues.html`, `project_plan_template.md`).

## Testing Guidelines
There is no automated test suite in this template. Validate changes by regenerating outputs with `support/scripts/issues.py` and opening the HTML report to confirm filters, counts, and sort order. If you add tests, document the tooling in `README.md` and keep them lightweight.

## Commit & Pull Request Guidelines
Git history currently contains a single short message (`initial push`), so no strict convention is established. Use concise, present-tense summaries (example: "add issue export flag") and keep commits focused. For PRs, include:
- A brief summary of changes and affected directories.
- Regeneration steps if outputs in `support/bugmgmt/exports/` or `support/ui/` were updated.
- Screenshots for UI/template changes.

## Security & Configuration Tips
All assets are local and PII-free by design. Keep issue data sanitized, and prefer `--data` / `--output` flags to keep generated files inside this repo.
