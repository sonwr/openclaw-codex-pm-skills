# Web QA Playwright replay fixture sequence

Use this sequence when a strict-plus report is failing and you want the shortest reproducible fixture path before opening the full report.

1. Run the isolated fixture that matches the visible blocker.
2. Confirm the JSON output names the same blocker family.
3. Repair that blocker in the real report.
4. Re-run the strict-plus validator on the real report.
5. Only expand to another fixture when the first blocker is green.

## Fast fixture order

1. `examples/web_qa_playwright_strict_fail_missing_timestamp_only.md` — missing chronology fields
2. `examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md` — timestamp order drift
3. `examples/web_qa_playwright_strict_fail_status_inconsistency_only.md` — checkpoint/check mismatch
4. `examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md` — missing evidence paths
5. `examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md` — reused artifact refs
6. `examples/web_qa_playwright_strict_fail_missing_recovery_owner_only.md` — missing owner handoff

## Rule of thumb

- Chronology problems first.
- Evidence-path problems second.
- Owner handoff wording last.

That ordering keeps replay repair deterministic: fix whether the run can be replayed before polishing who should receive the handoff.
