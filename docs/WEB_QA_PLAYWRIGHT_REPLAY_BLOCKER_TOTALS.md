# Playwright Replay Blocker Totals

Use this note when strict-plus validation already exposed replay blocker totals and you need to turn that count into a fast handoff decision.

## What the total means

- `0` blockers: the report is replay-clean for the currently validated scope.
- `1` blocker: keep the handoff narrow and name the single blocked lane directly.
- `2-3` blockers: summarize the hotspot section first, then list the failed check ids that still need repair.
- `4+` blockers: do not write a vague rerun request; route by hotspot section or owner before replay.

## Fast handoff rule

1. Start with the blocker total.
2. Name the hottest blocked section or failed lane.
3. Add the owner or next action only if the validator output already supports it.
4. Avoid claiming signoff-ready status when the total is non-zero.

## Example status lines

- `Replay blockers: 0 — validator-clean and safe for replay-ready handoff.`
- `Replay blockers: 1 — keep the rerun scoped to the failing lane and attach the failing check ids.`
- `Replay blockers: 3 — route by hotspot section first; do not flatten into a generic rerun note.`

## When to open other docs

- Need the hotspot tie-break rule? Open `docs/WEB_QA_PLAYWRIGHT_REPLAY_HOTSPOT_TIEBREAK.md`.
- Need a rerun-only handoff checklist? Open `docs/WEB_QA_PLAYWRIGHT_RERUN_HANDOFF_CARD.md`.
- Need owner-oriented wording after validation passes? Open `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_OWNER_SEQUENCE.md`.
