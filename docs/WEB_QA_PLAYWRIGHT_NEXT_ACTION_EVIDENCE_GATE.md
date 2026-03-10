# WEB_QA_PLAYWRIGHT_NEXT_ACTION_EVIDENCE_GATE

Use this quick gate after validation passes but before calling a blocked artifact replay-ready.

## Fast check

Confirm the `Next action:` line includes all three:

1. at least one failed check id,
2. at least one stable target ref (for example `ref=e12`),
3. at least one artifact path or screenshot/log proof target.

## Decision

- If all three are present, the next action is evidence-anchored enough for rerun handoff.
- If failed check ids are present but refs or artifact proof are missing, treat the artifact as validator-clean but not replay-ready.
- If the next action does not name a failed check id, rewrite it before handoff so repair scope is explicit.

## Copy-ready reminder

`Next action:` should say which failed lane to repair, where to act, and what proof to capture on the rerun.
