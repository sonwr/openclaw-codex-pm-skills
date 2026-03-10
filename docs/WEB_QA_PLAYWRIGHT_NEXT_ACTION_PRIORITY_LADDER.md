# Web QA Playwright next-action priority ladder

Use this ladder when a blocked or mixed-signoff run already exposes replay metadata, but the operator still needs one short rule for what to repair first.

## Priority ladder

1. **Target refs are unstable** — fix selector / target drift before touching other fields.
2. **Evidence is missing** — restore screenshot, trace, or artifact paths next so reruns produce believable proof.
3. **Chronology is broken** — repair timestamp or checkpoint ordering before broadening scope.
4. **State consistency is unclear** — resolve checkpoint/check status mismatches after the replay path is trustworthy.
5. **Owner handoff is incomplete** — assign the recovery owner and the next action before leaving the report blocked.

## Quick operator prompts

- Can the same target be replayed without guessing?
- Does the current run include the proof artifacts needed for signoff?
- Do checkpoint times and sequence make sense on the first read?
- Are failed checks aligned with checkpoint status?
- Is there a named owner plus an explicit next action?

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_BLOCKER_PRIORITY.md`
- `docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_REPAIR_LANE_CARD.md`
