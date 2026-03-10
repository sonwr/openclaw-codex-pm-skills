# WEB_QA_PLAYWRIGHT_SIGNOFF_COVERAGE_CARD

Use this card when a strict-plus validation run passes but signoff coverage is still incomplete.

## Quick read

1. Check `signoff_field_coverage_rate`.
2. Read `missing_signoff_fields`.
3. Decide whether the artifact is:
   - **validation-clean** — parser contract passed, but a human signoff field is still missing
   - **handoff-ready** — every required signoff field is present
4. If `next_action` is missing, add one deterministic repair/handoff sentence before asking another operator to continue.

## Copy-ready prompts

- **Validation-clean, not handoff-ready**: "Validation passed, but signoff coverage is incomplete. Add the missing signoff field(s) before handoff."
- **Handoff-ready**: "Validation passed and signoff coverage is complete. Safe to hand off without reopening the report."

## Pair with

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_MISSING_FIELDS.md`
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md`
- `docs/WEB_QA_PLAYWRIGHT_JSON_HANDOFF.md`
