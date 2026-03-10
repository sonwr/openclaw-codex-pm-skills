# WEB_QA_PLAYWRIGHT_SIGNOFF_FIRST_LOOK

Use this note when a strict-plus report already passed validation and you need the fastest possible signoff scan before handoff.

## 60-second order

1. Confirm `Replay readiness` is present and matches the failed-check reality.
2. Check `Regressions` against the actual FAIL checklist count.
3. Read `Next action` and confirm it points to the next deterministic rerun or handoff.
4. If the run is BLOCKED, confirm the next action includes the failed check ids that matter most.
5. If signoff still feels ambiguous, open `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md` for the deeper review order.

## Quick interpretation

- `READY` + no failed checks + explicit next action -> handoff-ready.
- `READY` + missing next action -> validation-clean but signoff-incomplete.
- `BLOCKED` + failed checks referenced in next action -> rerun-ready handoff.
- `BLOCKED` + no failed check refs in next action -> repair the signoff text before routing.

## Pair with

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md`
- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_COVERAGE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`
