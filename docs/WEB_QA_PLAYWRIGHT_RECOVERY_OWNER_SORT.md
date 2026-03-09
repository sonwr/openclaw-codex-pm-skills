# Web QA Playwright recovery-owner sort

Use this note when a blocked run has multiple failed checks and you need a deterministic repair order by owner before rerunning Playwright.

## Sort order

1. Group failed checks by `Recovery owner` from the report.
2. Within each owner, keep the original failed-check order (`F1`, `F2`, `V1`, ...).
3. Repair the owner with the largest number of failed checks first.
4. If two owners have the same number of failed checks, pick the owner whose first failed check appears earlier in the report.
5. After each owner lane is repaired, rerun the smallest section that still covers the unresolved checks.

## Why this helps

- Keeps multi-owner handoffs deterministic for CI and human triage.
- Prevents rerunning the whole suite before the dominant owner lane is repaired.
- Matches the replay-ready style used by `report_metadata.failed_check_ids_by_recovery_owner` and related summaries.

## Example

If the failed checks are:

- `F2` / `F4` → `frontend`
- `V1` → `design-system`
- `O1` / `O3` / `O4` → `backend`

Repair order should be:

1. `backend` (`O1`, `O3`, `O4`)
2. `frontend` (`F2`, `F4`)
3. `design-system` (`V1`)

Then rerun only the sections that still contain unresolved checks instead of replaying the whole report.
