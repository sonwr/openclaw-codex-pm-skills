# Web QA Playwright scenario-report signoff

Use this note when a Web QA artifact depends on governance-sandbox scenario files plus markdown/html report proof.

## Fast loop

1. Validate the Web QA artifact first.
2. Re-run the linked governance scenario fixture that produced the report.
3. Confirm the markdown/html report still names the same scenario context, hotspot, and next action.
4. Only call the handoff signoff-ready when both the validator and the scenario-report bundle stay aligned.

## Minimum evidence

- validator PASS output
- scenario file path or stdin proof
- report.json / report.md / report.html bundle
- one sentence describing whether the next action stayed lane-scoped or expanded

## Hold language

Use hold language when the validator passes but the scenario/report bundle is stale, missing, or points at a different replay lane than the current artifact.
