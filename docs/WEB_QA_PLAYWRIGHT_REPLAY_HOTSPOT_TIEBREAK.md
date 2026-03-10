# Web QA Playwright replay hotspot tie-break guide

Use this quick rule when multiple sections report the same replay hotspot load.

## Tie-break order

1. Start with the section that has the highest hotspot blocker count.
2. If sections are tied, prefer the section with the highest checkpoint share.
3. If sections are still tied, use the validator's ordered section priority: `functional`, `visual`, `off_happy`.
4. Keep the runner-up sections in the handoff so follow-up work is not lost.

## Why this matters

A deterministic tie-break lets PM, QA, and automation handoff tools pick the same first repair target without debating section order on every rerun.

## Recommended handoff copy

- Primary hotspot: `functional`
- Runner-up hotspot(s): `visual`
- Repair summary: fix the primary blocker first, then rerun the tied runner-up sections if the first repair does not clear the report.
