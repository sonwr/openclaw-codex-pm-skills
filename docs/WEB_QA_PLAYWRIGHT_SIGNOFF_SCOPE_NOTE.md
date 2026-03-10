# Web QA Playwright signoff scope note

Use this note when a report is validator-clean but the handoff should stay intentionally narrow.

## Use this when

- the blocked lane is already obvious,
- the owner is known,
- the next action is replayable,
- but the artifact should **not** be described as a whole-run signoff.

## Compact wording pattern

`Validator pass. Signoff scope stays limited to <lane/section> for <owner>; rerun or repair outside that scope is not yet requested.`

## What this note prevents

- over-claiming that the entire run is handoff-ready,
- blurring a hotspot rerun into a full replay request,
- hiding unresolved owner or evidence gaps outside the named scope.

## Minimum evidence to include

1. the blocked lane or section,
2. the owner or recovery lane,
3. the proof artifact or target ref,
4. the exact rerun or repair boundary.

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_GATE.md`
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_RERUN_SPLIT.md`
- `docs/WEB_QA_PLAYWRIGHT_RERUN_SCOPE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_BOUNDARY.md`
