# Delivery Process (Template)

Use this process to keep changes small, reviewable, and persona-driven. Copy/adapt for new projects.

## Fast start (per session)
- Read: `DOCS/process.md`, `DOCS/projectplan.md`, `DOCS/project_wide_docs/personas.md`.
- Pick project/phase from `projectplan`; open the phase definition/action plan and linked stage actions (if any).
- Run personas (Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead by default); add others only if triggered.
- Execute, validate, update docs/DoD, and log issues/lessons.

## Initial setup (template only)
- If you are creating a new project from this template and the repo hasn’t been renamed yet, start with the **Project Creator/Owner** persona:
  - Choose the project name and update `DOCS/projectplan.md` and `DOCS/projects/<project>/` paths accordingly (rename the sample project if needed).
  - Capture the project purpose, scope boundaries, and initial phases in `projectplan.md` and the project summary file.
  - Decide whether to keep the sample BugMgmt module/UI and the LaTeX user-doc template; remove or keep per your needs.
  - After naming, continue with the default personas (Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead).

## Source-of-truth stack
- **Project plan:** `DOCS/projectplan.md` lists active projects and links to `DOCS/projects/<project>/`.
- **Project directory:** project summary plus phases.
- **Phase definition:** per phase, with objective/scope/completion and stage list.
- **Phase action plan:** per phase, listing stages and persona actions, validation, and checklists.
- **Stage action file:** per stage, with persona sections and acceptance for that slice of work. Naming: `DOCS/projects/<project>/phases/phase<NN>/actions/<project>_phase<NN>_stage<name>_action.md`.
- **Templates:** `DOCS/templates/` for project plan, phase definitions/action plans, stage actions, review checklists, and DoD.

## Personas (defaults)
- Start with: Reviewer/Sponsor → Product/Process Manager → Developer → QA Lead.
- Add others from `DOCS/project_wide_docs/personas.md` when scope triggers them (Docs Expert, Architect, Security, UI/Accessibility, etc.).

## Standard flow for a phase/stage
1. Read the project plan and the current project’s phase definition/action plan.
2. Create or open the stage action file(s) under the phase `actions/` folder using the naming convention.
3. Run personas and record outputs in the stage action file (use `DOCS/templates/review_checklists.md`).
4. Execute the work and run the changed scripts yourself; QA Lead/Test Engineering validate; Docs Expert updates docs when in scope.
5. Close-out: complete the DoD checklist, log lessons, and mark the phase/stage done in the phase action plan and project plan.

## Quality gates (apply to every stage action)
- Expected behaviours/counts/filters and data scope are recorded before coding; note any temporary fallbacks and expiry conditions.
- Outputs are deterministic (ordering/filenames) and JSON-safe (no NaN/Infinity) where relevant.
- Data handling documented; avoid PII unless explicitly required for your project.
- DoD completed with test commands/results captured; issues log updated with learnings.

## Naming and directories
- **Project plan:** `DOCS/projectplan.md`.
- **Project directory:** `DOCS/projects/<project>/` with project summary and phases.
- **Phase directory:** `DOCS/projects/<project>/phases/phase<NN>/` with `phase_definition.md` and `action_plan_phase<NN>.md`.
- **Stage actions:** `DOCS/projects/<project>/phases/phase<NN>/actions/<project>_phase<NN>_stage<name>_action.md`.
- **Templates:** `DOCS/templates/` (project/phase/action/review/DoD).

## Context start macro
At the start of a new context:
- Read `DOCS/process.md`, `DOCS/projectplan.md`, `DOCS/project_wide_docs/personas.md`, the current project’s phase definition/action plan, and linked stage action files.
- Report: current project(s) and their active phases; for the chosen project, list the current phase/stage and active stage action files. List the persona catalog.
- Ask: which persona to activate next (default Reviewer/Sponsor). Note any project-wide action if applicable.
