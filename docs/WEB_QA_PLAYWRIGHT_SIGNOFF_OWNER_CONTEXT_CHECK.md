# WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CONTEXT_CHECK

Use this quick check when the validator passes but the signoff still feels too thin for owner handoff.

## 30-second context check

Confirm all three are visible before calling the artifact owner-ready:

1. **Owner cue** — who should take the next action?
2. **Failure lane** — which blocked lane or failed check still matters?
3. **Proof target** — which artifact or rerun output should the owner update next?

## Copy-ready line

`Validator PASS, but keep handoff scoped to <owner> on <lane/check> until <artifact or rerun proof> is refreshed.`

## When to escalate to a fuller note

Use a longer handoff instead of the one-line note when:

- multiple owners still share the same unresolved lane,
- the next artifact is unclear,
- or the next action no longer points at a stable rerun boundary.
