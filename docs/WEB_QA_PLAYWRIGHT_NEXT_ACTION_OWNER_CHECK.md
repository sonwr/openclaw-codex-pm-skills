# WEB_QA_PLAYWRIGHT_NEXT_ACTION_OWNER_CHECK

Use this quick check before telling someone a strict-plus next action is ready for owner handoff.

## Owner check

1. Confirm the `Next action:` sentence names the blocker lane that actually dominates the replay metadata.
2. Check whether the sentence already implies the right owner class (selector fix, evidence capture, state reset, or product issue).
3. If the owner is still ambiguous, add the owner cue before adding extra execution detail.
4. Keep the sentence tied to one rerun target and one proof artifact so the owner can act immediately.
5. Make sure the line still fits as a copy-ready handoff without reopening the full JSON.

## Pass signal

A passing next-action handoff should tell the receiver who owns the first repair move, which blocked lane goes first, and what proof must come back on the rerun.
