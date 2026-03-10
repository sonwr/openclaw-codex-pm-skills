# WEB_QA_PLAYWRIGHT_SIGNOFF_HANDOFF_SEQUENCE

Use this when a Playwright web QA report already passes validation, but you still need a tight signoff-ready handoff.

## Fast sequence

1. Confirm the report already passed the strict-plus validator.
2. Read `failed_checks` and `replay_blocker_totals` together before writing the handoff.
3. Verify that every unresolved failed check has an owner, target, or explicit escalation reason.
4. Re-read `next_action` and keep it scoped to the hottest blocked lane.
5. Only call the report signoff-ready when the next action names the lane, proof target, and expected rerun artifact.

## Output pattern

Use a compact handoff sentence with four parts:

- current validator state,
- hottest blocked lane,
- named owner or escalation path,
- next rerun or repair proof.

Example:

> Validator PASS, checkout lane still blocked by missing signed-in replay proof, owner is product-auth QA, rerun after fresh trace plus screenshot bundle.

## When to avoid signoff-ready wording

Do **not** call the report signoff-ready yet when any of these remain true:

- owner coverage is still partial,
- `next_action` is generic,
- hotspot sections tie without a resolved lead,
- replay evidence is missing even though validation passed.
