# WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_EXAMPLES

Copy-ready next-action examples for signoff handoff notes.

## Why this exists

When a run fails, reviewers often know the blocker but leave the next action too vague.
These examples keep handoff notes specific enough for replay, rerun scoping, and owner routing.

## Formula

Use this structure when writing the next action:

```text
Repair <failure dimension> for <scope> using <artifact or target refs>, then rerun <checks or section>.
```

## Example lines

- Repair missing timestamp evidence for `functional` checkpoints `F1-F3` using `artifacts/run-2026-03-10/`, then rerun failed checks `C1-C3`.
- Repair duplicated target refs for `visual` checkpoint `V2` using the latest DOM snapshot and screenshot bundle, then rerun the visual section only.
- Repair missing artifact refs for owner `frontend-qa` across `C4` and `C5`, then rerun the affected signoff lane before merge review.
- Repair checkpoint/check status mismatch in `off-happy-path` scope using the replay log from the last CI run, then rerun the section summary export.

## Anti-patterns

Avoid handoff text like:

- `Investigate this failure`
- `Fix signoff issues`
- `Try rerunning the suite`

These lines do not explain what to repair, which scope to rerun, or which evidence to use.

## Minimal checklist

A good next-action line should answer all three:

1. What is broken?
2. What scope should be rerun?
3. What evidence or refs anchor the replay?
