# Stage Action (project_management_phase03_stage_consolidation_under_single_directory_action.md)

- **Phase/Stage:** Phase 03 — Consolidation under single directory.
- **Objective:** Consolidate process, BugMgmt, and project management assets under `AI_first/` and update references.
- **Scope:** In: inventory PM docs/UI assets, move planning docs to `AI_first/projects/`, remove empty workspace directories, path/link updates, doc rendering checks. Out: content redesign or automation.
- **Acceptance:** Assets live under `AI_first/`; empty workspace directories removed; references updated in project/phase docs and `AI_first/ui/PM.html`; docs render without broken links.
- **Dependencies/data:** `AI_first/docs/projectplan.md`, `AI_first/projects/project_management/`, `AI_first/ui/PM.html`, `AI_first/ui/project_project_management.html`, `AI_first/ui/docs/`.
- **Outputs:** Asset inventory, consolidation plan, updated paths, validation notes.
- **Definition of Done:** Acceptance met; persona notes filled; validation captured.

## Personas (record outputs; use `AI_first/docs/templates/review_checklists.md`)
- Reviewer/Sponsor:
- Project/Process Manager: Confirmed the drop-in goal: keep all process/BugMgmt/PM artifacts under `AI_first/`, remove empty workspace dirs, and update docs/scripts to point at `AI_first/projects/`.
- Developer:
- QA Lead:
- Docs Expert:
- Architect/Security/Ops/Perf/DBA/UI (if triggered):

## Plan
- Inventory PM-related files and current references.
- Set `AI_first/` as the target root and `AI_first/projects/` as the planning docs root.
- Move files, remove empty workspace directories, and update links/paths.
- Regenerate docs and validate links.

## Execution notes
- Pending.

## Validation
- Run `python3 AI_first/scripts/render_docs.py` and spot-check PM links.
- Confirm `AI_first/ui/PM.html` references resolve.

## Documentation updates
- Update `AI_first/docs/projectplan.md`, process docs, and README/AGENTS with new paths.

## Issues & lessons
- Pending.
