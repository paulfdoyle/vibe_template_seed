# Delivery Process (Template)

Use this process to keep changes small, reviewable, and persona-driven. Copy/adapt for new projects.

## Fast start (per session)
- Read: `support/docs/process.md`, `support/docs/projectplan.md`, `support/docs/project_wide_docs/personas.md`.
- Pick project/phase from `projectplan`; open the phase definition/action plan and linked stage actions (if any).
- Open a multi-context working set: project plan, phase docs, and the active stage action file in separate windows.
- Run personas (Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead by default); add others only if triggered.
- Execute, validate, update docs/DoD, and log issues/lessons.

## Multi-context working set
- Keep three windows open: `support/docs/projectplan.md`, the active phase definition/action plan, and the current stage action file.
- Keep the persona catalog (`support/docs/project_wide_docs/personas.md`) accessible; use it to decide when to add specialist reviews.
- Treat the stage action file as the working scratchpad: log decisions, validations, and DoD checks as you go.

## Initial setup (template only)
- If you are creating a new project from this template, copy the repo to a new working location and treat the template as read-only.
- If the repo hasn’t been renamed yet, start with the **Project Creator/Owner** persona:
  - Choose the project name and update `support/docs/projectplan.md` and `projects/<project>/` paths accordingly (rename the sample project if needed).
  - Capture the project purpose, scope boundaries, and initial phases in `projectplan.md` and the project summary file.
  - Decide whether to keep the sample BugMgmt module/UI and the LaTeX user-doc template; remove or keep per your needs.
  - After naming, continue with the default personas (Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead).

## Project initialization (optional)
- Run `python3 support/scripts/init_project.py --project <project> --prefix <PREFIX> --owner "Name"` to scaffold `projects/<project>/`, update `support/docs/projectplan.md`, and register BugMgmt prefixes.
- The script also creates `support/ui/project_<project>.html` and updates `support/ui/PM.html` with the new row.
- After running, regenerate formatted docs via `python3 support/scripts/render_docs.py`.

## Repo layout (support vs workspace)
- `support/`: template process docs, BugMgmt tooling, and UI reports/styles.
- `projects/`: project planning docs (summaries, phases, stage actions).
- `src/`, `tests/`, `config/`, `data/`, `assets/`, `scripts/`, `docs/`: your product workspace (code, tests, configs, assets, docs).

## Documentation rendering
- While editing markdown under `support/docs/` or `projects/`, run `python3 support/scripts/watch_docs.py` from the repo root to auto-render `support/ui/docs/`.
- If you are not running the watcher, run `python3 support/scripts/render_docs.py` after doc changes.

## Source-of-truth stack
- **Project plan:** `support/docs/projectplan.md` lists active projects and links to `projects/<project>/`.
- **Project directory:** project summary plus phases.
- **Phase definition:** per phase, with objective/scope/completion and stage list.
- **Phase action plan:** per phase, listing stages and persona actions, validation, and checklists.
- **Stage action file:** per stage, with persona sections and acceptance for that slice of work. Naming: `projects/<project>/phases/phase<NN>/actions/<project>_phase<NN>_stage<name>_action.md`.
- **Templates:** `support/docs/templates/` for project plan, phase definitions/action plans, stage actions, review checklists, and DoD.

## Personas (defaults)
- Start with: Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead.
- Add others from `support/docs/project_wide_docs/personas.md` when scope triggers them (Docs Expert, Architect, Security, UI/Accessibility, etc.).

## Standard flow for a phase/stage
1. Read the project plan and the current project’s phase definition/action plan.
2. Create or open the stage action file(s) under the phase `actions/` folder using the naming convention.
3. Run personas and record outputs in the stage action file (use `support/docs/templates/review_checklists.md`).
4. Execute the work and run the changed scripts yourself; QA Lead/Test Engineering validate; Docs Expert updates docs when in scope.
5. Close-out: complete the DoD checklist, log lessons, and mark the phase/stage done in the phase action plan and project plan.

## Quality gates (apply to every stage action)
- Expected behaviours/counts/filters and data scope are recorded before coding; note any temporary fallbacks and expiry conditions.
- Outputs are deterministic (ordering/filenames) and JSON-safe (no NaN/Infinity) where relevant.
- Data handling documented; avoid PII unless explicitly required for your project.
- DoD completed with test commands/results captured; issues log updated with learnings.

## Bug management (BugMgmt module)
- Source of truth is `support/bugmgmt/issues/issues.jsonl` (one JSON object per line). Do not edit exports directly.
- Required fields: `id`, `date`, `project`, `phase`, `stage`, `area`, `status`, `severity`, `summary`, `owner` (defaults from `BUGMGMT_REPO_OWNER` or `git config user.name`, with optional overrides in `PROJECT_OWNERS` when set to `unassigned`).
- ID format uses a project-based prefix (example: `BMG-2025-01-001`). Configure prefixes in `support/scripts/issues.py` (`PROJECT_PREFIXES`, e.g., `BMG`, `PMG`).
- For new bugs, include detail fields: `root_cause`, `proposed_fix`, `qa_reproduction` (QA reproduction steps).
- Example entry (single line):
  ```json
  {"id":"BMG-2025-01-003","date":"2025-01-07","project":"bugmgmt","phase":"01","stage":"foundation","area":"docs","status":"open","severity":"minor","summary":"Short description","owner":"unassigned","root_cause":"TBD","proposed_fix":"TBD","qa_reproduction":"TBD"}
  ```
- Use status values `open`, `in_progress`, `closed` and severity values `critical`, `major`, `minor`, `nit`.
- Create a new entry when a bug is found; update the same entry when status or ownership changes.
- After any bug change (new entry or status/field update), regenerate exports; the HTML report must be recreated each time:
  - `python3 support/scripts/issues.py list --format json --output support/bugmgmt/exports/json/bugmgmt_issues.json`
  - `python3 support/scripts/issues.py list --format html --output support/ui/bugmgmt_issues.html`
- View locally via `file://` at `support/ui/bugmgmt_issues.html`; filters and counts should match the JSONL store.

## Naming and directories
- **Project plan:** `support/docs/projectplan.md`.
- **Project directory:** `projects/<project>/` with project summary and phases.
- **Phase directory:** `projects/<project>/phases/phase<NN>/` with `phase_definition.md` and `action_plan_phase<NN>.md`.
- **Stage actions:** `projects/<project>/phases/phase<NN>/actions/<project>_phase<NN>_stage<name>_action.md`.
- **Templates:** `support/docs/templates/` (project/phase/action/review/DoD).

## Context start macro
At the start of a new context:
- Read `support/docs/process.md`, `support/docs/projectplan.md`, `support/docs/project_wide_docs/personas.md`, the current project’s phase definition/action plan, and linked stage action files.
- Report: current project(s) and their active phases; for the chosen project, list the current phase/stage and active stage action files. List the persona catalog.
- Ask: which persona to activate next (default Reviewer/Sponsor). Note any project-wide action if applicable.
