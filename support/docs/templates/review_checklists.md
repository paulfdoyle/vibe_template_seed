# Review Checklists (Template)

## Reviewer/Sponsor
- Progress/quality/maintainability; blockers; go/no-go conditions.

## Project/Process Manager
- Current phase/stage and definition of done; next steps/owners; dependencies/risks/blockers; process gaps; handoffs/approvals.

## Product Manager
- Acceptance criteria; user/business rules; scope in/out; gaps/questions.

## Developer
- Implementation notes; deviations; side effects/tech debt; logging/telemetry needs.

## QA Lead
- Edge cases/invariants; validation needs; test ideas; data/fixtures/term codes; acceptance signals.

## QA Engineer
- Regression/smoke checks (commands/suites); coverage gaps; quick sanity checks.

## Docs Specialist
- Docs/paths to update; consistency/link/version/glossary fixes; clarity issues; release-note/acceptance updates; doc debt.

## Architect (when triggered)
- Decision (approve/conditions/redesign); risks (boundaries, security/privacy, performance/capacity, failure modes, data integrity, operational fit); conditions to accept.

## Security/Privacy (when triggered)
- Threats; secrets/PII handling; injection/supply-chain risks; data minimisation/logging hygiene; mitigations/requirements.

## Ops/Observability (when triggered)
- Logging quality (no PII/noise); metrics/alerts; rollout/rollback/flags; migration/backward compatibility; ops risks/runbook needs.

## Performance/Cost (when triggered)
- Perf/cost risks; benchmarks/datasets; acceptance thresholds; scaling/cost options.

## DBA (when triggered)
- Schema/migration impacts; integrity/lineage risks; backup/rollback; perf/indexing; access/security concerns.

## UI/Accessibility (when triggered)
- A11y/usability checks; blockers/must-fix; clarity/design issues.
