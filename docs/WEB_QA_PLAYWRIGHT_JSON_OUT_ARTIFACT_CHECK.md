# WEB_QA_PLAYWRIGHT_JSON_OUT_ARTIFACT_CHECK

Use this when a strict-plus run already passed or failed and you only need a fast check that the saved `--json-out` artifact is still handoff-ready.

## Fast check

1. Confirm the artifact exists where CI expects it.
2. Open the JSON and verify these fields exist:
   - `status`
   - `active_profile_preset`
   - `counts.functional` / `counts.visual` / `counts.off_happy`
   - `report_metadata.signoff_field_coverage_rate`
   - `report_metadata.next_action_failed_check_refs`
3. If the run is meant for deterministic replay, confirm the preset is one of:
   - `strict-plus`
   - `playwright-interactive-profile`
   - `deterministic-replay-profile`
   - `strict-replay-profile`
   - `ci-replay-profile`
4. Reopen the matching markdown report only if the JSON is missing the handoff fields you need.

## Why this exists

The saved JSON should be enough for CI parsing and replay triage. Reopening the full report is slower and easier to derail when you only need the artifact contract.
