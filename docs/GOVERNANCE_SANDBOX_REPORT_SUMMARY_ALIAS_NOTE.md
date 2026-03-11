# governance-sandbox report summary alias note

Use this note when one scenario file needs to carry reviewer-facing memo context into generated markdown and HTML reports.

## Rule

Prefer `report.description` when the scenario already has a clear proposal/context pair and you need one extra reviewer-facing summary line for the generated memo.

## Why

- keeps reusable memo context in the scenario fixture instead of ad-hoc README prose
- lets markdown and HTML artifacts expose the same summary handoff
- keeps CLI proof and future web-demo proof aligned on one source field

## Minimal check

1. Put the reviewer-facing sentence in `report.description`.
2. Run the scenario-file flow that writes JSON + markdown + HTML artifacts.
3. Confirm the summary appears in both human-readable reports before handoff.
