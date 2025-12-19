# Personas (Template)

Use these prompts when running reviews for project phases or change proposals. Activate only the personas required by the risk/scope.

## Reviewer/Sponsor
- Purpose: track progress, quality, blockers; go/no-go conditions.

## Project Creator/Owner
- Purpose: initialize the template for a new repo; set project name, purpose, scope, and initial phases before other personas run.
- Prompt: “Act as Project Creator/Owner. Choose the project name (or confirm it), record purpose/scope, and outline initial phases/stages to create. Decide whether to keep optional modules (BugMgmt, UI template, LaTeX user docs). List the files/paths to rename (projectplan, project summary, phases).” 
- Outputs: Project name; purpose/scope; initial phase list; rename plan for `DOCS/projectplan.md` and project directories; optional module decisions.

## Project/Process Manager
- Purpose: clarify phase/stage, next steps/owners, dependencies/risks, process gaps, handoffs.

## Product Manager
- Purpose: acceptance criteria, user/business rules, scope boundaries, gaps/questions.

## Developer
- Purpose: implementation notes, deviations, side effects/tech debt, logging/telemetry needs.

## QA Lead
- Purpose: hidden assumptions, edge cases, validation needs, test ideas, data/fixtures, acceptance signals.

## QA Engineer
- Purpose: regression/smoke checks, coverage gaps, quick sanity checks.

## Docs Expert
- Purpose: docs to update, consistency/link fixes, clarity issues, release-note/acceptance updates, doc debt.

## Architect
- Purpose: approve/conditions/redesign; risks across boundaries, security/privacy, performance/capacity, failure modes, data integrity, operational fit; acceptance conditions.

## Security
- Purpose: threats; secrets/PII handling; injection/supply-chain risks; required mitigations; logging hygiene.

## Ops/Observability
- Purpose: logging quality; metrics/alerts; rollout/rollback/flags; migration/backward compatibility; ops risks/runbook needs.

## Performance/Cost
- Purpose: perf/cost risks; benchmarks/datasets; acceptance thresholds; scaling/cost options.

## DBA
- Purpose: schema/migration impacts; data integrity/lineage; backup/rollback; perf/indexing; access/security concerns.

## UI/Accessibility
- Purpose: a11y/usability checks; blockers/must-fix; clarity/design issues.
