# Vibe Template

A neutral, SRMS-free repo that packages the delivery process (personas, stage actions, DoD), the BugMgmt project, and a basic UI report template. Use this as a seed when creating new AI/VIBE-style projects.

## What you get
- `support/`: process docs, templates, BugMgmt tooling, and UI reports/styles.
- `projects/`: project planning docs (BugMgmt + Project Management).
- Workspace directories for your product: `src/`, `tests/`, `config/`, `data/`, `assets/`, `scripts/`, `docs/`.

## First-time flow (AI-first)
Describe the new repo and project to your agent; it will handle the steps below. Manual commands are included only if you are working without an agent.

1) Copy this repo to a new starter repo.
   - Example: `cp -R vibe_template_seed <new_repo_name>` or clone/rename.
   - Treat this template repo as read-only; do your work in the new repo.
   - Keep `support/` intact; put product work under `src/`, `tests/`, `config/`, `data/`, `assets/`, `scripts/`, `docs/`.
2) Activate the process.
   - Read `support/docs/process.md`, `support/docs/projectplan.md`, and `support/docs/project_wide_docs/personas.md`.
   - Open `index.html` (redirects to `support/ui/PM.html`) via `file://` and keep the stage action file open while you work.
   - While editing docs, run `python3 support/scripts/watch_docs.py` from the repo root to auto-render `support/ui/docs/` (manual fallback).
3) Initiate a new project.
   - Automated: `python3 support/scripts/init_project.py --project <project> --prefix <PREFIX> --owner "Name"`
   - Manual: copy `projects/_template/` to `projects/<project>/` and edit placeholders.
   - Then run `python3 support/scripts/render_docs.py` to refresh formatted docs after any doc edits.

## Optional setup
Use `python3` for the commands below; if your system maps `python` to Python 3, you can use `python` instead.
If you use a virtual environment, keep `.venv/` out of version control (this repo includes a `.gitignore`).
If you use BugMgmt, regenerate exports after any bug change:
```bash
python3 support/scripts/issues.py list --format json --output support/bugmgmt/exports/json/bugmgmt_issues.json
python3 support/scripts/issues.py list --format html --output support/ui/bugmgmt_issues.html
```
Open `support/ui/bugmgmt_issues.html` and `support/ui/PM.html` via `file://` to review.

## Optional modules
- BugMgmt: keep if you want local issue tracking; remove or ignore `support/bugmgmt/`, `support/ui/bugmgmt_issues.html`, and `support/scripts/issues.py` if not needed.
- UI template: extend `support/ui/templates/report_base.html` for lightweight static reports.
- LaTeX user docs: start from `support/docs/user_docs/user_doc_template.tex` if you want PDF user guides.

## Notes
- Sample data is PII-free and deterministic.
- All assets are local; no external network calls are required.
- Update paths via CLI flags or env vars (see `python3 support/scripts/issues.py --help`).
