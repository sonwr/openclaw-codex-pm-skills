# Web QA Playwright next-action retry note

Use this note when a failed run already has evidence, but the handoff still needs one clear retry sentence.

## When to use it
- The report already names the failed check ids.
- A rerun is appropriate after a small fix or environment reset.
- The next action should stay short enough to paste into a status update.

## One-line retry pattern
`Retry <failed-check-id> after <fix/reset>, capture <artifact refs>, and confirm whether the same blocker still reproduces.`

## Minimum handoff fields
- failed check id
- fix or reset cue
- artifact path to capture
- confirmation goal for the rerun

## Example
`Retry F2 after clearing the stale session cookie, capture artifacts/f2-rerun.png, and confirm whether the spinner timeout still reproduces.`
