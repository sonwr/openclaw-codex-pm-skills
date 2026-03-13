# Web QA Playwright result-card recovery bridge

Keep the result-card flow small and replayable.

- Preserve one primary status card that names the failed check ids, stable target refs, and saved artifact paths together.
- Re-run from the same browser target before widening scope or adding new checkpoints.
- Treat recovery as complete only after the updated report still passes the validator with the same handoff fields visible.
