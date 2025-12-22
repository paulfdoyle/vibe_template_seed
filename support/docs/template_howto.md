# Template Adoption Guide

Use this guide to spin up a new project from the Vibe Template.

## Setup
1) Copy or clone the template repo into your workspace.
   - Treat the template repo as read-only; do your work in the copied repo.
2) Optionally create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`.
   - Keep `.venv/` out of version control (the template includes a `.gitignore`).
3) Start the doc watcher if you want automatic updates while editing docs (from the repo root): `python3 support/scripts/watch_docs.py`.
4) Regenerate BugMgmt exports (if using BugMgmt):
   ```bash
   python3 support/scripts/issues.py list --format json --output support/bugmgmt/exports/json/bugmgmt_issues.json
   python3 support/scripts/issues.py list --format html --output support/ui/bugmgmt_issues.html
   ```
5) Open `support/ui/bugmgmt_issues.html` via file:// to confirm UI assets load locally.

## Process and personas
- Read `support/docs/process.md` for the standard flow and persona defaults.
- See `support/docs/project_wide_docs/personas.md` for persona prompts.
- Use templates under `support/docs/templates/` when adding projects/phases/stages.

## Starting a new project
Option A (automated):
1) Run `python3 support/scripts/init_project.py --project <project> --prefix <PREFIX> --owner "Name"`.
2) Review `support/ui/PM.html` and the new `support/ui/project_<project>.html` detail page.
3) Run `python3 support/scripts/render_docs.py` to refresh formatted docs.

Option B (manual):
1) Add a project entry to `support/docs/projectplan.md` with summary and phase roots.
2) Create `projects/<project>/project_summary_<project>.md`.
3) For each phase, add `phase_definition.md` and `action_plan_phase<NN>.md` under `phases/phase<NN>/`.
4) For each stage, add a stage action file under `phases/phase<NN>/actions/` using the naming convention.
5) Run personas and record outputs in the stage action files.

## Workspace layout
- Keep template tooling under `support/` and planning docs under `projects/`.
- Put product code in `src/`, tests in `tests/`, and configs/assets/data/scripts/docs in the corresponding workspace directories.

## BugMgmt module (optional)
- Data store: `support/bugmgmt/issues/issues.jsonl` (PII-free). Use `support/scripts/issues.py list --help` for flags.
- Exports: `support/bugmgmt/exports/json/bugmgmt_issues.json` and `support/ui/bugmgmt_issues.html`.
- UI: bundled assets under `support/ui/assets/` and `support/ui/style/`; works via file://.
- Toggle off: skip running the CLI and remove/ignore `support/bugmgmt/`, `support/ui/bugmgmt_issues.html`, `support/scripts/issues.py`.

## UI report template
- Base template at `support/ui/templates/report_base.html`; reuse bundled CSS in `support/ui/style/`.
- Duplicate and extend for new reports; keep assets local for offline usage.

## PII and determinism
- Sample data is PII-free. Keep your own data PII-free unless required.
- Maintain deterministic outputs (ordering, hashes) for repeatable runs.

## Troubleshooting
- If exports fail, verify paths or pass explicit `--data/--output` flags.
- If file:// fetch is blocked, the fallback data in `support/ui/bugmgmt_issues.html` will render; ensure assets are local.
