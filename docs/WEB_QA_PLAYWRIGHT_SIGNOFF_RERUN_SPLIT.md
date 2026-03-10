# Web QA Playwright signoff vs rerun split

Use this note when a report already passes validation and the team still needs to decide whether to stop at signoff or schedule another rerun.

## Pick signoff now when

- every failed check has been resolved or explicitly accepted,
- replay blockers are `0`,
- missing owner coverage is `0`,
- and the next action is documentation-only or release-only.

## Pick rerun now when

- validation passed but the report still references unresolved hotspot sections,
- target refs or artifact refs are still missing for a likely replay lane,
- a recovery owner handoff is incomplete,
- or the next action still depends on new evidence.

## Fast wording patterns

- **Signoff-ready:** `Validation passed, no replay blockers remain, and evidence is complete for signoff.`
- **Rerun-ready:** `Validation passed, but replay evidence is incomplete for <failed-check-id>; rerun that lane before signoff.`

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_EXIT_CRITERIA.md`
- `docs/WEB_QA_PLAYWRIGHT_RERUN_READINESS_CUES.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`
