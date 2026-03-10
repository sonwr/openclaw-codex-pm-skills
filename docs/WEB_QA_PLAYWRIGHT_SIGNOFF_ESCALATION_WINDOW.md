# Web QA Playwright Signoff Escalation Window

Use this quick rule when a run is technically complete but still not safe to sign off.

## Escalate now

Escalate before signoff when any of these are true:

- the top blocker stayed unchanged across two reruns
- the same section keeps failing after the recommended next action
- ownership is still unknown for a failed checkpoint
- evidence is partial and a downstream reviewer would have to guess

## Hold signoff locally

Keep the run local when all of these are true:

- the blocker is already classified
- the next action is concrete and reproducible
- the owner or lane is known
- a rerun is expected to add new evidence instead of repeating noise

## One-line handoff pattern

`Escalate signoff: <blocker> remains after <count> reruns; owner=<owner>; next_action=<action>.`
