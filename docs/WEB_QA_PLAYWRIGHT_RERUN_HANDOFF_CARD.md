# Web QA Playwright rerun handoff card

Use this card when a report already passed schema validation but still is not ready for a clean replay handoff.

## 60-second rerun decision

1. Confirm the failing or blocked check IDs named in `Next action`.
2. Confirm each referenced check has at least one stable target ref (`ref=e...`).
3. Confirm each referenced check has at least one artifact path for replay evidence.
4. Confirm the rerun owner is explicit when a repair must be delegated.
5. Confirm the rerun scope is narrow enough to avoid replaying unrelated sections.

## Good rerun handoff shape

- names the exact failed or blocked checks
- includes the target refs needed to reopen the page state
- includes artifact refs that show the last known failing state
- states whether the next step is rerun, repair, or owner triage
- keeps unrelated checkpoints out of the handoff summary

## Escalate instead of rerun when

- the next action omits the failing check IDs
- the same target ref is reused ambiguously across unrelated checkpoints
- artifacts are missing for the failing state
- owner coverage is incomplete and the team does not know who should repair first

## Suggested pairing docs

- `docs/WEB_QA_PLAYWRIGHT_REPLAY_READINESS_QUICKCHECK.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_SECTION_RERUN_CHECKLIST.md`
