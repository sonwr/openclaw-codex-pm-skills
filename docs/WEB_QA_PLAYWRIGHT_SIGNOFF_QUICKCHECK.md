# Web QA Playwright signoff quickcheck

Use this note when a strict-plus report already validates but you still need a fast human pass before commit, CI approval, or rerun handoff.

## 60-second review order

1. Confirm the report passes `scripts/validate_web_qa_report.py --strict-plus`.
2. Check the signoff block for `Result`, `Ready for rerun`, `Next action`, and owner/routing language.
3. Confirm the effective replay hotspot and next-step text match the failed checkpoints you would repair first.
4. Confirm at least one artifact path exists for every failed checkpoint named in the handoff.
5. Make sure section labels (`functional`, `visual`, `off_happy`) stay consistent between the execution log and the replay JSON.

## Quick questions

- Does the report tell the next operator what to repair first without rereading the whole log?
- Are failed checks grouped clearly enough for owner routing?
- Would a reviewer understand whether the run is blocked by missing refs, missing evidence, or chronology drift?
- Is the next action specific enough to rerun one lane instead of reopening the whole session?

## Good final handoff shape

A good strict-plus handoff usually leaves you with:

- one clear hotspot section,
- one clear blocker family,
- named failed checkpoints,
- artifact evidence already attached,
- and a copy-ready next action sentence.

If any of those are missing, treat the report as validation-clean but handoff-weak and repair the prose before signoff.
