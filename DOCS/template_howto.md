# Template Adoption Guide

Use this guide to spin up a new project from the Vibe Template.

## Setup
1) Copy or clone the template repo into your workspace.
2) Optionally create a virtual environment: `python -m venv .venv && source .venv/bin/activate`.
3) Regenerate BugMgmt exports (if using BugMgmt):
   ```bash
   python scripts/issues.py list --format json --output json-data/bugmgmt_issues.json
   python scripts/issues.py list --format html --output UI/bugmgmt_issues.html
   ```
4) Open `UI/bugmgmt_issues.html` via file:// to confirm UI assets load locally.

## Process and personas
- Read `DOCS/process.md` for the standard flow and persona defaults.
- See `DOCS/project_wide_docs/personas.md` for persona prompts.
- Use templates under `DOCS/templates/` when adding projects/phases/stages.

## Starting a new project
1) Add a project entry to `DOCS/projectplan.md` with summary and phase roots.
2) Create `DOCS/projects/<project>/project_summary_<project>.md`.
3) For each phase, add `phase_definition.md` and `action_plan_phase<NN>.md` under `phases/phase<NN>/`.
4) For each stage, add a stage action file under `phases/phase<NN>/actions/` using the naming convention.
5) Run personas and record outputs in the stage action files.

## BugMgmt module (optional)
- Data store: `issues/issues.jsonl` (PII-free). Use `scripts/issues.py list --help` for flags.
- Exports: `json-data/bugmgmt_issues.json` and `UI/bugmgmt_issues.html`.
- UI: bundled assets under `UI/assets/`; works via file://.
- Toggle off: skip running the CLI and remove/ignore `issues/`, `json-data/`, `UI/bugmgmt_issues.html`, `scripts/issues.py`.

## UI report template
- Base template at `UI/templates/report_base.html`; reuse bundled CSS in `UI/assets/`.
- Duplicate and extend for new reports; keep assets local for offline usage.

## PII and determinism
- Sample data is PII-free. Keep your own data PII-free unless required.
- Maintain deterministic outputs (ordering, hashes) for repeatable runs.

## Troubleshooting
- If exports fail, verify paths or pass explicit `--data/--output` flags.
- If file:// fetch is blocked, the fallback data in `UI/bugmgmt_issues.html` will render; ensure assets are local.
