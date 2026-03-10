# Web QA Playwright retry exit matrix

Use this matrix before spending another retry on a flaky or blocked run.

## Retry once more
- A selector, fixture, or assertion changed in the current patch.
- The failure is isolated to one page or one checkpoint.
- The evidence already explains the suspected root cause.
- A single rerun can confirm whether the fix actually landed.

## Stop retrying and hand off
- The same blocker repeats with no code or environment change.
- Multiple checkpoints fail for the same environment issue.
- Ownership is unclear after the second pass.
- The run no longer improves the signoff decision.

## What to record before exiting
- failing checkpoint and page
- owner or next owner
- last known good evidence
- exact reason another retry is not worth it
