# Web QA Playwright scenario recovery loop

Use this when an interactive replay run fails but the team still needs a deterministic next action.

1. Reproduce the failing step with the smallest stable path.
2. Confirm whether the blocker is locator drift, timing drift, or environment drift.
3. Keep the rerun request scoped to one hotspot unless evidence shows section-wide failure.
4. Attach the failed check id, affected page/section, and proof artifact path in the next-action line.
5. Re-run the validator before handoff so the replay note and artifact metadata stay aligned.
