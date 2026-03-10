# Web QA Playwright replay-readiness quickcheck

Use this when a report already passes validation but you need a fast human decision on whether it is truly ready for replay, rerun, or owner handoff.

## 60-second decision order

1. Confirm `Replay readiness` says `READY` or `BLOCKED`.
2. Confirm the hotspot section and blocker summary are explicit in the JSON artifact.
3. Confirm `Next action:` names the failed check ids that should drive the rerun.
4. Confirm checkpoint target refs and artifact refs exist for the first rerun lane.
5. Confirm the recovery owner is visible for every unresolved failed check.
6. Confirm missing signoff fields are either fixed or explicitly accepted for inspection-only review.

## Quick interpretation

- **Validation PASS + replay READY** → safe to treat as replay-ready evidence.
- **Validation PASS + replay BLOCKED** → safe to hand off, but only with the hotspot blocker and next step attached.
- **Validation PASS + missing owners / missing refs** → do not call it handoff-ready yet.

## Use with

- `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_QUICKCHECK.md`
- `docs/WEB_QA_PLAYWRIGHT_OWNER_TRIAGE_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_REPLAY_CARD.md`
- `docs/WEB_QA_PLAYWRIGHT_REPLAY_HOTSPOT_TIEBREAK.md`
