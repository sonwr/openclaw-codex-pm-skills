# WEB_QA_PLAYWRIGHT_NEXT_ACTION_RERUN_CUE

Use this card when the validator already says a report is PASS or FAIL, but you still need to decide whether the `Next action:` line gives operators a rerun-ready cue.

## Quick check

A rerun-ready next action should name:

1. the blocked or failing lane/check,
2. the stable target reference when available,
3. the proof artifact when available,
4. and the concrete rerun or repair move.

## Good pattern

`Next action: Rerun F2 on ref=e12 and capture artifacts/f2-login-error.png after selector repair.`

## Weak pattern

`Next action: Investigate and rerun later.`

## Decision rule

- If the sentence names the failing lane and the exact next move, it is usually rerun-usable.
- If target or artifact support is missing, keep the report in repair/handoff language instead of calling it replay-ready.
- If multiple lanes are blocked, start with the hottest hotspot before widening the rerun scope.
