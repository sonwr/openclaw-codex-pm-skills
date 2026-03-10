# Web QA Playwright signoff scope status line

Use this when the validator passes and you need a single line that keeps the handoff honest about scope.

## When to use it

Reach for this note when:

- the artifact is validator-clean,
- the next step is still lane- or section-scoped,
- and you want one sentence that does not overstate whole-run readiness.

## One-line template

`Validator PASS for <scope>, but signoff stays <scope>-scoped until <missing proof or rerun target> is closed.`

## Fast examples

- `Validator PASS for checkout, but signoff stays checkout-scoped until payment retry evidence is captured.`
- `Validator PASS for the search-results section, but signoff stays section-scoped until the unstable filter checkpoint is rerun.`
- `Validator PASS for hotspot lane C12, but signoff stays lane-scoped until the owner confirms the missing screenshot pair.`

## Quick check

Before posting the line, confirm that it names:

1. the passing scope,
2. the boundary that still applies,
3. and the exact proof or rerun target still missing.
