# Web QA Playwright signoff handoff ready signal

Use this note when a strict-plus report already validates and you need a compact answer to one question:

> Is this artifact merely validator-clean, or is it actually ready to hand to the next owner?

## Handoff-ready signal

Call the artifact **handoff-ready** only when all four checks are true:

1. **Blocked lane is named** — the summary points to the exact failed check ids or hotspot lane.
2. **Owner is obvious** — the next action makes the rerun owner or repair owner easy to identify.
3. **Proof is reusable** — screenshot, trace, log, or artifact refs are present and current.
4. **Scope is narrow** — the next action asks for one focused rerun/repair step instead of a vague full replay.

## Safe language when one check is missing

- "Validator PASS, but owner routing is still incomplete."
- "Validator PASS, but the next action is still too broad for handoff."
- "Validator PASS, but fresh proof artifacts are still missing for replay."

## Fast operator check

Before writing the final signoff sentence, confirm:

- failed check ids are visible,
- the hottest blocked lane is named,
- one owner-oriented next action exists,
- at least one proof artifact can be reopened without rerecording context.

If any item is missing, keep the artifact in **validation-clean / not handoff-ready** language.
