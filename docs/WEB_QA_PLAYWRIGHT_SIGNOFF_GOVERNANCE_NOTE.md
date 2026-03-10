# WEB_QA_PLAYWRIGHT_SIGNOFF_GOVERNANCE_NOTE

Use this note when the validator already passed but you still need to explain why the artifact is **not governance-ready yet**.

## When to use it

- validation is `PASS`
- replay evidence exists
- owner routing or next-action clarity is still incomplete
- you need one short sentence that does **not** overstate readiness

## Compact wording pattern

`Validator PASS confirms the report is structurally reviewable, but governance handoff is still blocked by <missing owner|missing next action|missing scope note>.`

## Short examples

- `Validator PASS confirms the report is structurally reviewable, but governance handoff is still blocked by missing owner assignment for the failing visual lane.`
- `Validator PASS confirms the report is structurally reviewable, but governance handoff is still blocked by a next action that does not yet name the replay target.`
- `Validator PASS confirms the report is structurally reviewable, but governance handoff is still blocked by unresolved section scope wording.`

## Exit check

Only drop the governance-blocked wording after the report has:

- explicit owner coverage,
- a concrete next action,
- and wording that matches the real replay scope.
