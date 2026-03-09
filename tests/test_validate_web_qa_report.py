from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.validate_web_qa_report import _build_report_metadata, validate_report_text


VALID_REPORT = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n- Viewport: `1366x768`\n- Test account: `qa.user@example.test`\n\n## 2) Checklist execution summary\n- Functional checks (5/5 pass)\n  - F1: PASS\n  - F2: PASS\n  - F3: PASS\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n- F3 checkpoint: Required-field validation blocked form submit\n- F4 checkpoint: Pressing Enter on password field triggered submit\n- F5 checkpoint: Logout redirected to `/login`\n- V1 checkpoint: Captured baseline layout screenshot\n- V2 checkpoint: Captured error-state screenshot\n- V3 checkpoint: Captured dashboard screenshot\n- O1 checkpoint: Wrong-password path stayed on `/login`\n- O2 checkpoint: Empty-password path showed client-side validation\n\n## 4) Signoff\n- Regressions: 0\n- Merge recommendation: **APPROVE**\n- Replay readiness: **READY**\n"""


FAILED_REPORT_WITH_RECOVERY = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n- Viewport: `1366x768`\n- Test account: `qa.user@example.test`\n\n## 2) Checklist execution summary\n- Functional checks (4/5 pass)\n  - F1: PASS\n  - F2: FAIL\n    - Expected: Login success toast appears within 2 seconds\n    - Observed: Spinner persisted for 10 seconds\n    - First failure timestamp: 2026-03-07T04:10:00Z\n    - Retry: FAIL\n    - Failure classification: product\n    - Evidence: `artifacts/f2-failure.png`\n  - F3: PASS\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n- F2 checkpoint: FAIL - Inline error panel missing after submit\n- F3 checkpoint: Required-field validation blocked form submit\n- F4 checkpoint: Pressing Enter on password field triggered submit\n- F5 checkpoint: Logout redirected to `/login`\n- V1 checkpoint: Captured baseline layout screenshot\n- V2 checkpoint: Captured error-state screenshot\n- V3 checkpoint: Captured dashboard screenshot\n- O1 checkpoint: Wrong-password path stayed on `/login`\n- O2 checkpoint: Empty-password path showed client-side validation\n\n## 4) Signoff\n- Regressions: 1\n- Merge recommendation: **BLOCK**\n- Replay readiness: **BLOCKED**\n"""


class ValidateWebQaReportTests(unittest.TestCase):
    def test_strict_fail_fixture_reports_duplicate_checkpoint_ids(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_duplicate_checkpoint.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(fixture_text, strict=True)
        self.assertTrue(any("duplicate checkpoint ids" in e for e in errors))

    def test_strict_fail_fixture_reports_missing_failure_evidence(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_evidence.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(fixture_text, strict=True)
        self.assertTrue(any("Evidence:" in e for e in errors))

    def test_strict_fail_fixture_reports_missing_failure_classification(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_classification.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(fixture_text, strict=True)
        self.assertTrue(any("Failure classification:" in e for e in errors))

    def test_strict_fail_fixture_reports_malformed_failure_breakdown(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_malformed_failure_breakdown.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(
            fixture_text,
            require_failure_classification_summary=True,
        )
        self.assertTrue(any("failure classification summary" in e for e in errors))

    def test_strict_fail_fixture_reports_missing_execution_log_header(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_execution_log_header.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(fixture_text, strict=True)
        self.assertTrue(any("Execution log" in e for e in errors))

    def test_validate_report_passes_in_strict_mode_for_valid_report(self) -> None:
        self.assertEqual(validate_report_text(VALID_REPORT, strict=True), [])

    def test_validate_report_fails_when_visual_screenshot_refs_missing(self) -> None:
        broken = VALID_REPORT.replace("`shots/v3.png`", "")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("screenshot references" in e for e in errors))

    def test_validate_report_fails_when_scope_preconditions_missing(self) -> None:
        broken = VALID_REPORT.replace("- Test account: `qa.user@example.test`\n", "")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("test account" in e for e in errors))

    def test_validate_report_fails_when_section_header_ratio_mismatch(self) -> None:
        broken = VALID_REPORT.replace("- Functional checks (5/5 pass)", "- Functional checks (4/5 pass)")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("header pass count" in e for e in errors))

    def test_validate_report_fails_when_check_ids_are_not_sequential(self) -> None:
        broken = VALID_REPORT.replace("  - F5: PASS", "  - F6: PASS")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("F1..F5" in e for e in errors))

    def test_validate_report_passes_when_failures_include_recovery_fields(self) -> None:
        self.assertEqual(validate_report_text(FAILED_REPORT_WITH_RECOVERY, strict=True), [])

    def test_validate_report_fails_when_visual_check_has_no_inline_evidence(self) -> None:
        broken = VALID_REPORT.replace("  - V2: PASS `shots/v2.png`", "  - V2: PASS")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("every visual check line" in e for e in errors))

    def test_validate_report_fails_when_failure_recovery_fields_missing(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace("    - Observed: Spinner persisted for 10 seconds\n", "")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("Observed:" in e for e in errors))

    def test_validate_report_fails_when_failure_timestamp_missing(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - First failure timestamp: 2026-03-07T04:10:00Z\n", ""
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("First failure timestamp:" in e for e in errors))

    def test_validate_report_fails_when_failure_evidence_missing(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Evidence: `artifacts/f2-failure.png`\n", ""
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("Evidence:" in e for e in errors))

    def test_validate_report_fails_when_failure_classification_missing(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Failure classification: product\n", ""
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("Failure classification:" in e for e in errors))

    def test_validate_report_fails_when_next_action_does_not_reference_failed_check_id(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY + "- Next action: Investigate spinner timeout and update release checklist\n"
        errors = validate_report_text(
            broken,
            require_next_action=True,
            require_next_action_failed_check_ref=True,
        )
        self.assertTrue(any("failed check id" in e for e in errors))

    def test_validate_report_passes_when_next_action_references_failed_check_id(self) -> None:
        fixed = FAILED_REPORT_WITH_RECOVERY + "- Next action: Investigate F2 spinner timeout, capture new artifacts, and rerun login flow\n"
        self.assertEqual(
            validate_report_text(
                fixed,
                require_next_action=True,
                require_next_action_failed_check_ref=True,
            ),
            [],
        )

    def test_validate_report_fails_when_next_action_does_not_reference_all_failed_check_ids(self) -> None:
        report = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n\n## 2) Checklist execution summary\n- Functional checks (3/5 pass)\n  - F1: PASS\n  - F2: FAIL\n    - Expected: Inline selector resolves after submit\n    - Observed: Locator never resolved\n    - First failure timestamp: 2026-03-07T04:10:00Z\n    - Retry: FAIL\n    - Failure classification: selector\n    - Recovery owner: qa-ui\n    - Evidence: `artifacts/f2-failure.png`\n  - F3: FAIL\n    - Expected: Spinner clears within 2 seconds\n    - Observed: Spinner persisted for 10 seconds\n    - First failure timestamp: 2026-03-07T04:12:00Z\n    - Retry: FAIL\n    - Failure classification: runtime\n    - Recovery owner: qa-runtime\n    - Evidence: `artifacts/f3-failure.png`\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F2 checkpoint: FAIL - selector missing after submit\n- F3 checkpoint: FAIL - spinner never cleared\n\n## 4) Signoff\n- Regressions: 2\n- Merge recommendation: **BLOCK**\n- Replay readiness: **BLOCKED**\n- Next action: Investigate F2 selector drift, capture fresh evidence, and rerun selector coverage\n"""
        errors = validate_report_text(
            report,
            require_next_action=True,
            require_next_action_all_failed_check_refs=True,
        )
        self.assertTrue(any("every failed check id" in e for e in errors))


    def test_report_metadata_exposes_next_action_failed_check_refs(self) -> None:
        report = FAILED_REPORT_WITH_RECOVERY + "- Next action: Investigate F2 spinner timeout, capture new artifacts, and rerun login flow\n"
        metadata = _build_report_metadata(report)

        self.assertEqual(metadata["failed_check_ids"], ["F2"])
        self.assertTrue(metadata["has_next_action"])
        self.assertEqual(metadata["next_action_text"], "Investigate F2 spinner timeout, capture new artifacts, and rerun login flow")
        self.assertEqual(metadata["next_action_failed_check_refs"], ["F2"])
        self.assertEqual(metadata["next_action_failed_check_ref_count"], 1)
        self.assertEqual(metadata["next_action_failed_check_coverage_rate"], 1.0)
        self.assertEqual(metadata["next_action_target_refs"], [])
        self.assertEqual(metadata["next_action_target_ref_count"], 0)
        self.assertEqual(metadata["next_action_artifact_refs"], [])
        self.assertEqual(metadata["next_action_artifact_ref_count"], 0)
        self.assertTrue(metadata["next_action_mentions_rerun"])
        self.assertEqual(metadata["failed_check_classification_counts"], {"selector": 0, "runtime": 0, "product": 1})
        self.assertEqual(
            metadata["next_action_failed_check_coverage_rate_by_classification"],
            {"selector": 1.0, "runtime": 1.0, "product": 1.0},
        )
        self.assertEqual(
            metadata["unresolved_failed_check_coverage_rate_by_classification"],
            {"selector": 0.0, "runtime": 0.0, "product": 0.0},
        )
        self.assertEqual(metadata["checkpoint_section_counts"], {"functional": 5, "visual": 3, "off_happy": 2})


    def test_report_metadata_tracks_partial_next_action_coverage_by_classification(self) -> None:
        report = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n- Viewport: `1366x768`\n- Test account: `qa.user@example.test`\n\n## 2) Checklist execution summary\n- Functional checks (3/5 pass)\n  - F1: PASS\n  - F2: FAIL\n    - Expected: Inline selector resolves after submit\n    - Observed: Locator never resolved\n    - First failure timestamp: 2026-03-07T04:10:00Z\n    - Retry: FAIL\n    - Failure classification: selector\n    - Recovery owner: qa-ui\n    - Evidence: `artifacts/f2-failure.png`\n  - F3: FAIL\n    - Expected: Spinner clears within 2 seconds\n    - Observed: Spinner persisted for 10 seconds\n    - First failure timestamp: 2026-03-07T04:12:00Z\n    - Retry: FAIL\n    - Failure classification: runtime\n    - Recovery owner: qa-runtime\n    - Evidence: `artifacts/f3-failure.png`\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n- F2 checkpoint: FAIL - selector missing after submit\n- F3 checkpoint: FAIL - spinner never cleared\n- F4 checkpoint: Pressing Enter on password field triggered submit\n- F5 checkpoint: Logout redirected to `/login`\n- V1 checkpoint: Captured baseline layout screenshot\n- V2 checkpoint: Captured error-state screenshot\n- V3 checkpoint: Captured dashboard screenshot\n- O1 checkpoint: Wrong-password path stayed on `/login`\n- O2 checkpoint: Empty-password path showed client-side validation\n\n## 4) Signoff\n- Regressions: 2\n- Merge recommendation: **BLOCK**\n- Replay readiness: **BLOCKED**\n- Next action: Investigate F2 selector drift, capture fresh evidence, and rerun selector coverage\n"""
        metadata = _build_report_metadata(report)

        self.assertEqual(metadata["failed_check_classification_counts"], {"selector": 1, "runtime": 1, "product": 0})
        self.assertEqual(
            metadata["next_action_failed_check_coverage_rate_by_classification"],
            {"selector": 1.0, "runtime": 0.0, "product": 1.0},
        )
        self.assertEqual(
            metadata["unresolved_failed_check_coverage_rate_by_classification"],
            {"selector": 0.0, "runtime": 1.0, "product": 0.0},
        )

    def test_report_metadata_tracks_signoff_section_presence(self) -> None:
        metadata = _build_report_metadata(VALID_REPORT)
        self.assertTrue(metadata["has_signoff_section"])

        without_signoff = VALID_REPORT.replace("## 4) Signoff\n", "")
        metadata_without_signoff = _build_report_metadata(without_signoff)
        self.assertFalse(metadata_without_signoff["has_signoff_section"])

    def test_report_metadata_tracks_signoff_field_status_and_coverage(self) -> None:
        pass_metadata = _build_report_metadata(VALID_REPORT)
        self.assertEqual(
            pass_metadata["signoff_field_status"],
            {
                "regressions": "present",
                "merge_recommendation": "present",
                "replay_readiness": "present",
                "next_action": "missing",
            },
        )
        self.assertEqual(
            pass_metadata["present_signoff_fields"],
            ["regressions", "merge_recommendation", "replay_readiness"],
        )
        self.assertEqual(pass_metadata["missing_signoff_fields"], ["next_action"])
        self.assertEqual(pass_metadata["signoff_field_coverage_rate"], 0.75)

        fail_metadata = _build_report_metadata(
            FAILED_REPORT_WITH_RECOVERY
            + "- Next action: Investigate F2 spinner timeout, capture new artifacts, and rerun login flow\n"
        )
        self.assertEqual(fail_metadata["missing_signoff_fields"], [])
        self.assertEqual(fail_metadata["present_signoff_field_count"], 4)
        self.assertEqual(fail_metadata["signoff_field_coverage_rate"], 1.0)

    def test_report_metadata_blocks_ready_signoff_when_checkpoint_refs_are_missing(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_target_refs.md"
        )
        metadata = _build_report_metadata(fixture_path.read_text(encoding="utf-8"))

        self.assertEqual(metadata["replay_readiness"], "READY")
        self.assertEqual(metadata["effective_replay_readiness"], "BLOCKED")
        self.assertTrue(metadata["replay_readiness_effective_changed"])
        self.assertFalse(metadata["replay_readiness_consistent_with_failed_checks"] is False)
        self.assertIn("replay_readiness=READY but checkpoint target refs are missing for F1, F2, F3, F4, F5, V1, V2, V3, O1, O2", metadata["replay_readiness_blockers"])
        self.assertIn("replay_readiness=READY but checkpoint evidence refs are incomplete for F1, F2, F3, F4, F5, V1, V2, V3, O1, O2", metadata["replay_readiness_blockers"])
        self.assertEqual(
            metadata["replay_readiness_blocker_keys"],
            ["missing_target_refs", "incomplete_evidence_refs"],
        )
        self.assertEqual(
            metadata["replay_readiness_blocker_counts"],
            {
                "blocked_without_regressions": 0,
                "ready_with_regressions": 0,
                "missing_target_refs": 1,
                "missing_artifact_refs": 0,
                "incomplete_evidence_refs": 1,
                "missing_timestamps": 0,
            },
        )
        self.assertEqual(metadata["replay_readiness_blocker_count"], 2)
        self.assertEqual(
            metadata["replay_readiness_blocker_count_by_section"],
            {"functional": 10, "visual": 6, "off_happy": 4},
        )
        self.assertEqual(
            metadata["replay_readiness_blocker_keys_by_section"],
            {
                "functional": ["missing_target_refs", "incomplete_evidence_refs"],
                "visual": ["missing_target_refs", "incomplete_evidence_refs"],
                "off_happy": ["missing_target_refs", "incomplete_evidence_refs"],
            },
        )
        self.assertEqual(
            metadata["replay_readiness_blocker_coverage_rate_by_section"],
            {"functional": 2.0, "visual": 2.0, "off_happy": 2.0},
        )
        self.assertEqual(
            metadata["effective_replay_readiness_blocker_keys_by_section"],
            {
                "functional": ["missing_target_refs", "incomplete_evidence_refs"],
                "visual": ["missing_target_refs", "incomplete_evidence_refs"],
                "off_happy": ["missing_target_refs", "incomplete_evidence_refs"],
            },
        )
        self.assertEqual(
            metadata["effective_replay_readiness_blocker_count_by_section"],
            {"functional": 10, "visual": 6, "off_happy": 4},
        )
        self.assertEqual(
            metadata["effective_replay_readiness_blocker_coverage_rate_by_section"],
            {"functional": 2.0, "visual": 2.0, "off_happy": 2.0},
        )


    def test_report_metadata_marks_missing_next_action_for_clean_pass_reports(self) -> None:
        metadata = _build_report_metadata(VALID_REPORT)

        self.assertFalse(metadata["has_next_action"])
        self.assertIsNone(metadata["next_action_text"])
        self.assertEqual(metadata["next_action_failed_check_refs"], [])

    def test_report_metadata_deduplicates_next_action_failed_check_refs(self) -> None:
        report = (
            FAILED_REPORT_WITH_RECOVERY
            + "- Next action: Investigate F2 spinner timeout, compare F2 artifacts, and rerun F2 with fresh evidence\n"
        )
        metadata = _build_report_metadata(report)

        self.assertEqual(metadata["next_action_failed_check_refs"], ["F2"])
        self.assertEqual(metadata["next_action_failed_check_ref_count"], 1)

    def test_report_metadata_exposes_next_action_refs_and_artifacts_for_replay_handoff(self) -> None:
        report = (
            FAILED_REPORT_WITH_RECOVERY
            + "- Next action: Re-run F2 using ref=e12, compare against ref=e44, attach `artifacts/f2-rerun.png` and `artifacts/f2-trace.zip`, then retry login\n"
        )
        metadata = _build_report_metadata(report)

        self.assertEqual(metadata["next_action_target_refs"], ["e12", "e44"])
        self.assertEqual(metadata["next_action_target_ref_count"], 2)
        self.assertEqual(metadata["next_action_artifact_refs"], ["artifacts/f2-rerun.png", "artifacts/f2-trace.zip"])
        self.assertEqual(metadata["next_action_artifact_ref_count"], 2)
        self.assertTrue(metadata["next_action_mentions_rerun"])

    def test_report_metadata_exposes_partial_qa_inventory_coverage_for_triage(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_partial_check_refs_only.md"
        )
        metadata = _build_report_metadata(fixture_path.read_text(encoding="utf-8"))

        self.assertEqual(metadata["qa_inventory_check_ref_count"], 9)
        self.assertEqual(metadata["qa_inventory_check_ref_coverage_rate"], 0.9)
        self.assertEqual(metadata["qa_inventory_missing_check_refs"], ["O2"])
        self.assertEqual(metadata["qa_inventory_missing_check_ref_count"], 1)

    def test_report_metadata_distinguishes_missing_vs_reused_checkpoint_refs(self) -> None:
        missing_target_fixture = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_target_refs.md"
        )
        reused_target_fixture = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_target_ref_reuse_only.md"
        )
        missing_artifact_fixture = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_artifact_paths_only.md"
        )

        missing_target = _build_report_metadata(missing_target_fixture.read_text(encoding="utf-8"))
        reused_target = _build_report_metadata(reused_target_fixture.read_text(encoding="utf-8"))
        missing_artifact = _build_report_metadata(missing_artifact_fixture.read_text(encoding="utf-8"))

        self.assertEqual(
            missing_target["missing_checkpoint_target_ref_ids"],
            ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"],
        )
        self.assertEqual(missing_target["checkpoint_target_ref_count"], 0)
        self.assertEqual(missing_target["checkpoint_evidence_ref_coverage_rate"], 0.0)
        self.assertEqual(missing_target["missing_checkpoint_evidence_ref_count"], 10)
        self.assertEqual(
            missing_target["missing_checkpoint_evidence_ref_count_by_section"],
            {"functional": 5, "visual": 3, "off_happy": 2},
        )
        self.assertEqual(
            missing_target["missing_checkpoint_target_ref_count_by_section"],
            {"functional": 5, "visual": 3, "off_happy": 2},
        )
        self.assertEqual(
            missing_target["missing_checkpoint_target_ref_coverage_rate_by_section"],
            {"functional": 1.0, "visual": 1.0, "off_happy": 1.0},
        )

        self.assertEqual(reused_target["checkpoint_target_ref_count"], 9)
        self.assertEqual(reused_target["checkpoint_reused_target_refs"], ["login.shared"])
        self.assertEqual(reused_target["checkpoint_reused_target_ref_count"], 1)
        self.assertEqual(reused_target["checkpoint_evidence_ref_coverage_rate"], 1.0)

        self.assertEqual(missing_artifact["missing_checkpoint_artifact_ref_ids"], ["F3"])
        self.assertEqual(missing_artifact["checkpoint_artifact_ref_count"], 9)
        self.assertEqual(missing_artifact["checkpoint_evidence_ref_coverage_rate"], 0.9)
        self.assertEqual(missing_artifact["missing_checkpoint_evidence_ref_ids"], ["F3"])
        self.assertEqual(
            missing_artifact["missing_checkpoint_evidence_ref_count_by_section"],
            {"functional": 1, "visual": 0, "off_happy": 0},
        )
        self.assertEqual(
            missing_artifact["missing_checkpoint_artifact_ref_count_by_section"],
            {"functional": 1, "visual": 0, "off_happy": 0},
        )
        self.assertEqual(
            missing_artifact["missing_checkpoint_artifact_ref_coverage_rate_by_section"],
            {"functional": 0.2, "visual": 0.0, "off_happy": 0.0},
        )

    def test_validate_report_fails_when_failure_timestamp_not_iso_utc(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "2026-03-07T04:10:00Z", "2026-03-07 04:10:00 UTC"
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("ISO-8601 UTC timestamp format" in e for e in errors))

    def test_report_metadata_exposes_checkpoint_timestamp_coverage_for_replay_triage(self) -> None:
        timestamped = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: PASS 2026-03-08T14:40:00Z URL changed to `/dashboard`, user avatar visible",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: PASS 2026-03-08T14:41:00Z Captured baseline layout screenshot",
        )
        metadata = _build_report_metadata(timestamped)

        self.assertEqual(
            metadata["checkpoint_timestamps_by_id"],
            {"F1": "2026-03-08T14:40:00Z", "V1": "2026-03-08T14:41:00Z"},
        )
        self.assertEqual(metadata["checkpoint_timestamp_count"], 2)
        self.assertEqual(
            metadata["checkpoint_timestamp_count_by_section"],
            {"functional": 1, "visual": 1, "off_happy": 0},
        )
        self.assertEqual(
            metadata["missing_checkpoint_timestamp_ids"],
            ["F2", "F3", "F4", "F5", "V2", "V3", "O1", "O2"],
        )
        self.assertEqual(metadata["missing_checkpoint_timestamp_count"], 8)
        self.assertEqual(
            metadata["missing_checkpoint_timestamp_count_by_section"],
            {"functional": 4, "visual": 2, "off_happy": 2},
        )
        self.assertEqual(metadata["checkpoint_timestamp_coverage_rate"], 0.2)
        self.assertEqual(
            metadata["checkpoint_timestamp_coverage_rate_by_section"],
            {"functional": 0.2, "visual": 0.3333, "off_happy": 0.0},
        )
        self.assertEqual(
            metadata["missing_checkpoint_timestamp_coverage_rate_by_section"],
            {"functional": 0.8, "visual": 0.6667, "off_happy": 1.0},
        )

    def test_validate_report_fails_when_failure_timestamps_are_not_monotonic(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "  - F3: PASS\n",
            "  - F3: FAIL\n"
            "    - Expected: Required-field validation blocks submit\n"
            "    - Observed: Submit endpoint called unexpectedly\n"
            "    - First failure timestamp: 2026-03-07T04:05:00Z\n"
            "    - Retry: FAIL\n"
            "    - Failure classification: product\n"
            "    - Evidence: `artifacts/f3-failure.png`\n",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit\n",
            "- F3 checkpoint: FAIL - Required-field validation did not block submit\n",
        ).replace(
            "- Regressions: 1\n",
            "- Regressions: 2\n",
        )
        errors = validate_report_text(
            broken,
            strict=True,
            enforce_failure_timestamp_order=True,
        )
        self.assertTrue(any("failed-check First failure timestamp values must be monotonic" in e for e in errors))

    def test_validate_report_fails_when_status_token_not_normalized(self) -> None:
        broken = VALID_REPORT.replace("  - O2: PASS", "  - O2: OK")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("normalized status token PASS/FAIL" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_log_missing(self) -> None:
        broken = VALID_REPORT.replace("- O2 checkpoint: Empty-password path showed client-side validation\n", "")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("execution log must include checkpoint lines" in e for e in errors))

    def test_validate_report_fails_when_execution_log_section_header_missing(self) -> None:
        broken = VALID_REPORT.replace("## 3) Execution log\n", "## 3) Run trace\n")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("Execution log" in e for e in errors))

    def test_validate_report_fails_when_signoff_section_header_missing(self) -> None:
        broken = VALID_REPORT.replace("## 4) Signoff\n", "## 4) Final status\n")
        errors = validate_report_text(broken, require_signoff_section=True)
        self.assertTrue(any("signoff section" in e for e in errors))

    def test_validate_report_passes_when_signoff_section_header_present(self) -> None:
        self.assertEqual(validate_report_text(VALID_REPORT, require_signoff_section=True), [])

    def test_validate_report_fails_when_replay_readiness_missing(self) -> None:
        broken = VALID_REPORT.replace("- Replay readiness: **READY**\n", "")
        errors = validate_report_text(broken, require_replay_readiness=True)
        self.assertTrue(any("Replay readiness:" in e for e in errors))

    def test_validate_report_fails_when_zero_regression_replay_readiness_is_blocked(self) -> None:
        broken = VALID_REPORT.replace("- Replay readiness: **READY**", "- Replay readiness: **BLOCKED**")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("replay readiness must be READY" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_log_contains_duplicate_ids(self) -> None:
        broken = VALID_REPORT.replace(
            "- O2 checkpoint: Empty-password path showed client-side validation\n",
            "- O2 checkpoint: Empty-password path showed client-side validation\n"
            "- O2 checkpoint: Duplicate checkpoint line\n",
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("duplicate checkpoint ids" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_log_contains_unknown_id(self) -> None:
        broken = VALID_REPORT.replace(
            "- O2 checkpoint: Empty-password path showed client-side validation\n",
            "- O2 checkpoint: Empty-password path showed client-side validation\n"
            "- X1 checkpoint: Unknown section check\n",
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("unknown checkpoint ids" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_order_is_not_deterministic(self) -> None:
        broken = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n"
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n"
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n",
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("must follow deterministic order" in e for e in errors))

    def test_validate_report_fails_when_regression_count_mismatches_fail_lines(self) -> None:
        broken = VALID_REPORT.replace("- Regressions: 0", "- Regressions: 1")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("regressions count must match checklist FAIL count" in e for e in errors))

    def test_validate_report_fails_when_zero_regression_signoff_blocks_merge(self) -> None:
        broken = VALID_REPORT.replace("- Merge recommendation: **APPROVE**", "- Merge recommendation: **BLOCK**")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("must be APPROVE when regressions are 0" in e for e in errors))

    def test_validate_report_fails_when_regressions_present_but_merge_is_approve(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace("- Merge recommendation: **BLOCK**", "- Merge recommendation: **APPROVE**")
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("must be BLOCK when regressions are present" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_format_is_not_action_arrow_verify(self) -> None:
        errors = validate_report_text(VALID_REPORT, enforce_checkpoint_format=True)
        self.assertTrue(any("checkpoint format" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_format_is_action_arrow_verify(self) -> None:
        fixed = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: Submit valid credentials -> URL changed to `/dashboard` and user avatar visible",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Submit invalid credentials -> inline error panel rendered and focus moved to form alert",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: Submit empty required fields -> required-field validation blocked form submit",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: Press Enter on password field -> submit triggered",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: Click logout -> redirected to `/login`",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Capture baseline layout screenshot -> image stored in artifacts",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Capture error-state screenshot -> image stored in artifacts",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Capture dashboard screenshot -> image stored in artifacts",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: Submit wrong password -> stayed on `/login`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: Submit empty password -> client-side validation shown",
        )
        self.assertEqual(validate_report_text(fixed, enforce_checkpoint_format=True), [])

    def test_validate_report_fails_when_checkpoint_format_has_empty_verification(self) -> None:
        broken = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: Submit valid credentials -> ",
        )
        errors = validate_report_text(broken, enforce_checkpoint_format=True)
        self.assertTrue(any("invalid: F1" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_format_has_empty_action(self) -> None:
        broken = VALID_REPORT.replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: -> client-side validation shown",
        )
        errors = validate_report_text(broken, enforce_checkpoint_format=True)
        self.assertTrue(any("checkpoint format" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_timestamp_is_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, require_checkpoint_timestamps=True)
        self.assertTrue(any("checkpoint timestamps" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_timestamps_are_present(self) -> None:
        timestamped = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible @ 2026-03-07T05:00:01Z",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert @ 2026-03-07T05:00:02Z",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: Required-field validation blocked form submit @ 2026-03-07T05:00:03Z",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: Pressing Enter on password field triggered submit @ 2026-03-07T05:00:04Z",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: Logout redirected to `/login` @ 2026-03-07T05:00:05Z",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Captured baseline layout screenshot @ 2026-03-07T05:00:06Z",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Captured error-state screenshot @ 2026-03-07T05:00:07Z",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Captured dashboard screenshot @ 2026-03-07T05:00:08Z",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: Wrong-password path stayed on `/login` @ 2026-03-07T05:00:09Z",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: Empty-password path showed client-side validation @ 2026-03-07T05:00:10Z",
        )
        self.assertEqual(validate_report_text(timestamped, require_checkpoint_timestamps=True), [])

    def test_validate_report_passes_when_checkpoint_timestamps_are_monotonic(self) -> None:
        timestamped = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible @ 2026-03-07T05:00:01Z",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert @ 2026-03-07T05:00:02Z",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: Required-field validation blocked form submit @ 2026-03-07T05:00:03Z",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: Pressing Enter on password field triggered submit @ 2026-03-07T05:00:04Z",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: Logout redirected to `/login` @ 2026-03-07T05:00:05Z",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Captured baseline layout screenshot @ 2026-03-07T05:00:06Z",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Captured error-state screenshot @ 2026-03-07T05:00:07Z",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Captured dashboard screenshot @ 2026-03-07T05:00:08Z",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: Wrong-password path stayed on `/login` @ 2026-03-07T05:00:09Z",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: Empty-password path showed client-side validation @ 2026-03-07T05:00:10Z",
        )
        self.assertEqual(
            validate_report_text(timestamped, enforce_monotonic_checkpoint_timestamps=True),
            [],
        )

    def test_validate_report_fails_when_checkpoint_timestamps_are_not_monotonic(self) -> None:
        broken = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible @ 2026-03-07T05:00:05Z",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert @ 2026-03-07T05:00:04Z",
        )
        errors = validate_report_text(broken, enforce_monotonic_checkpoint_timestamps=True)
        self.assertTrue(any("checkpoint timestamp order" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_status_tokens_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, enforce_checkpoint_status_tokens=True)
        self.assertTrue(any("checkpoint status tokens" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_status_tokens_present(self) -> None:
        with_status = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: PASS - URL changed to `/dashboard`, user avatar visible",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: PASS - Inline error panel rendered and focus moved to form alert",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: PASS - Required-field validation blocked form submit",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: PASS - Pressing Enter on password field triggered submit",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: PASS - Logout redirected to `/login`",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: PASS - Captured baseline layout screenshot",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: PASS - Captured error-state screenshot",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: PASS - Captured dashboard screenshot",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: PASS - Wrong-password path stayed on `/login`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: PASS - Empty-password path showed client-side validation",
        )
        self.assertEqual(validate_report_text(with_status, enforce_checkpoint_status_tokens=True), [])

    def test_validate_report_fails_when_checkpoint_check_status_consistency_missing(self) -> None:
        errors = validate_report_text(
            VALID_REPORT,
            enforce_checkpoint_to_check_status_consistency=True,
        )
        self.assertTrue(any("status consistency" in e for e in errors))

    def test_validate_report_fails_when_checkpoint_check_status_consistency_mismatch(self) -> None:
        with_status_mismatch = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: FAIL - URL changed to `/dashboard`, user avatar visible",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: PASS - Inline error panel rendered and focus moved to form alert",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: PASS - Required-field validation blocked form submit",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: PASS - Pressing Enter on password field triggered submit",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: PASS - Logout redirected to `/login`",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: PASS - Captured baseline layout screenshot",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: PASS - Captured error-state screenshot",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: PASS - Captured dashboard screenshot",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: PASS - Wrong-password path stayed on `/login`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: PASS - Empty-password path showed client-side validation",
        )
        errors = validate_report_text(
            with_status_mismatch,
            enforce_checkpoint_to_check_status_consistency=True,
        )
        self.assertTrue(any("mismatch: F1" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_check_statuses_match(self) -> None:
        with_consistent_status = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: PASS - URL changed to `/dashboard`, user avatar visible",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: PASS - Inline error panel rendered and focus moved to form alert",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: PASS - Required-field validation blocked form submit",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: PASS - Pressing Enter on password field triggered submit",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: PASS - Logout redirected to `/login`",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: PASS - Captured baseline layout screenshot",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: PASS - Captured error-state screenshot",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: PASS - Captured dashboard screenshot",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: PASS - Wrong-password path stayed on `/login`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: PASS - Empty-password path showed client-side validation",
        )
        self.assertEqual(
            validate_report_text(
                with_consistent_status,
                enforce_checkpoint_to_check_status_consistency=True,
            ),
            [],
        )

    def test_validate_report_fails_when_visual_checkpoint_evidence_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, require_visual_checkpoint_evidence=True)
        self.assertTrue(any("visual checkpoint evidence" in e for e in errors))

    def test_validate_report_fails_when_execution_log_contains_non_checkpoint_bullet(self) -> None:
        broken = VALID_REPORT.replace(
            "- O2 checkpoint: Empty-password path showed client-side validation\n",
            "- O2 checkpoint: Empty-password path showed client-side validation\n"
            "- Notes: kept browser session alive for retry context\n",
        )
        errors = validate_report_text(
            broken,
            require_execution_log_step_count_match=True,
        )
        self.assertTrue(any("execution log step count" in e for e in errors))

    def test_validate_report_passes_when_execution_log_has_exact_checkpoint_steps(self) -> None:
        self.assertEqual(
            validate_report_text(
                VALID_REPORT,
                require_execution_log_step_count_match=True,
            ),
            [],
        )

    def test_validate_report_fails_when_execution_log_checkpoint_order_mismatch(self) -> None:
        broken = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n"
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n"
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n",
        )
        errors = validate_report_text(
            broken,
            require_execution_log_step_count_match=True,
        )
        self.assertTrue(any("checkpoint ids must exactly match deterministic order" in e for e in errors))

    def test_validate_report_fails_when_qa_inventory_section_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, require_qa_inventory_section=True)
        self.assertTrue(any("qa inventory" in e for e in errors))

    def test_validate_report_passes_when_qa_inventory_section_present(self) -> None:
        with_inventory = VALID_REPORT.replace(
            "## Scope\n",
            "## 1) QA inventory\n- Claim: Login works for valid user -> Checks: F1, F4\n\n## Scope\n",
        )
        self.assertEqual(
            validate_report_text(with_inventory, require_qa_inventory_section=True),
            [],
        )

    def test_validate_report_passes_when_visual_checkpoint_evidence_present(self) -> None:
        with_visual_evidence = VALID_REPORT.replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Captured baseline layout screenshot `shots/v1.png`",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Captured error-state screenshot `shots/v2.png`",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Captured dashboard screenshot `shots/v3.png`",
        )
        self.assertEqual(
            validate_report_text(
                with_visual_evidence,
                require_visual_checkpoint_evidence=True,
            ),
            [],
        )

    def test_validate_report_fails_when_checkpoint_artifact_paths_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, require_checkpoint_artifact_paths=True)
        self.assertTrue(any("checkpoint artifact paths" in e for e in errors))

    def test_strict_plus_missing_target_refs_only_fixture_isolates_single_traceability_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_target_refs.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(
            fixture_text,
            enforce_checkpoint_format=True,
            require_checkpoint_timestamps=True,
            enforce_monotonic_checkpoint_timestamps=True,
            enforce_checkpoint_status_tokens=True,
            require_visual_checkpoint_evidence=True,
            require_checkpoint_artifact_paths=True,
            require_checkpoint_target_refs=True,
            enforce_checkpoint_artifact_ref_uniqueness=True,
            require_failure_checkpoint_artifact_paths=True,
            require_failure_evidence_artifact_paths=True,
            require_failure_recovery_plan=True,
            require_failure_recovery_owner=True,
            enforce_checkpoint_to_check_status_consistency=True,
            require_failure_classification_summary=True,
            require_execution_log_step_count_match=True,
            require_qa_inventory_section=True,
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("checkpoint target refs", errors[0])

    def test_validate_report_accepts_video_artifact_paths_for_checkpoint_replay(self) -> None:
        with_video_artifact = VALID_REPORT.replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Captured baseline layout screenshot `artifacts/v1.mp4`",
        ).replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible `artifacts/f1.log`",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert `artifacts/f2.log`",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: Required-field validation blocked form submit `artifacts/f3.log`",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: Pressing Enter on password field triggered submit `artifacts/f4.log`",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: Logout redirected to `/login` `artifacts/f5.log`",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Captured error-state screenshot `shots/v2.png`",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Captured dashboard screenshot `shots/v3.png`",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: Wrong-password path stayed on `/login` `artifacts/o1.trace`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: Empty-password path showed client-side validation `artifacts/o2.trace`",
        )
        self.assertEqual(
            validate_report_text(
                with_video_artifact,
                require_checkpoint_artifact_paths=True,
            ),
            [],
        )

    def test_validate_report_passes_when_checkpoint_artifact_paths_present(self) -> None:
        with_artifacts = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible `artifacts/f1.log`",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert `artifacts/f2.log`",
        ).replace(
            "- F3 checkpoint: Required-field validation blocked form submit",
            "- F3 checkpoint: Required-field validation blocked form submit `artifacts/f3.log`",
        ).replace(
            "- F4 checkpoint: Pressing Enter on password field triggered submit",
            "- F4 checkpoint: Pressing Enter on password field triggered submit `artifacts/f4.log`",
        ).replace(
            "- F5 checkpoint: Logout redirected to `/login`",
            "- F5 checkpoint: Logout redirected to `/login` `artifacts/f5.log`",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: Captured baseline layout screenshot `shots/v1.png`",
        ).replace(
            "- V2 checkpoint: Captured error-state screenshot",
            "- V2 checkpoint: Captured error-state screenshot `shots/v2.png`",
        ).replace(
            "- V3 checkpoint: Captured dashboard screenshot",
            "- V3 checkpoint: Captured dashboard screenshot `shots/v3.png`",
        ).replace(
            "- O1 checkpoint: Wrong-password path stayed on `/login`",
            "- O1 checkpoint: Wrong-password path stayed on `/login` `artifacts/o1.trace`",
        ).replace(
            "- O2 checkpoint: Empty-password path showed client-side validation",
            "- O2 checkpoint: Empty-password path showed client-side validation `artifacts/o2.trace`",
        )
        self.assertEqual(
            validate_report_text(
                with_artifacts,
                require_checkpoint_artifact_paths=True,
            ),
            [],
        )

    def test_validate_report_fails_when_checkpoint_target_refs_missing(self) -> None:
        errors = validate_report_text(VALID_REPORT, require_checkpoint_target_refs=True)
        self.assertTrue(any("checkpoint target refs" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_target_refs_present(self) -> None:
        with_refs = (
            VALID_REPORT.replace("- F1 checkpoint:", "- F1 checkpoint: ref=f1-login ")
            .replace("- F2 checkpoint:", "- F2 checkpoint: ref=f2-error ")
            .replace("- F3 checkpoint:", "- F3 checkpoint: ref=f3-required ")
            .replace("- F4 checkpoint:", "- F4 checkpoint: ref=f4-enter ")
            .replace("- F5 checkpoint:", "- F5 checkpoint: ref=f5-logout ")
            .replace("- V1 checkpoint:", "- V1 checkpoint: ref=v1-layout ")
            .replace("- V2 checkpoint:", "- V2 checkpoint: ref=v2-error ")
            .replace("- V3 checkpoint:", "- V3 checkpoint: ref=v3-dashboard ")
            .replace("- O1 checkpoint:", "- O1 checkpoint: ref=o1-wrong-password ")
            .replace("- O2 checkpoint:", "- O2 checkpoint: ref=o2-empty-password ")
        )
        self.assertEqual(
            validate_report_text(
                with_refs,
                require_checkpoint_target_refs=True,
            ),
            [],
        )

    def test_strict_plus_target_ref_reuse_only_fixture_isolates_single_traceability_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_target_ref_reuse_only.md"
        )
        fixture_text = fixture_path.read_text(encoding="utf-8")
        errors = validate_report_text(
            fixture_text,
            enforce_checkpoint_format=True,
            require_checkpoint_timestamps=True,
            enforce_monotonic_checkpoint_timestamps=True,
            enforce_checkpoint_status_tokens=True,
            require_visual_checkpoint_evidence=True,
            require_checkpoint_artifact_paths=True,
            require_checkpoint_target_refs=True,
            enforce_checkpoint_target_ref_uniqueness=True,
            enforce_checkpoint_artifact_ref_uniqueness=True,
            require_failure_checkpoint_artifact_paths=True,
            require_failure_evidence_artifact_paths=True,
            require_failure_recovery_plan=True,
            require_failure_recovery_owner=True,
            enforce_checkpoint_to_check_status_consistency=True,
            require_failure_classification_summary=True,
            require_execution_log_step_count_match=True,
            require_qa_inventory_section=True,
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("target ref uniqueness", errors[0])

    def test_validate_report_fails_when_checkpoint_target_refs_are_not_unique(self) -> None:
        with_duplicate_ref = (
            VALID_REPORT.replace("- F1 checkpoint:", "- F1 checkpoint: ref=shared-ref ")
            .replace("- F2 checkpoint:", "- F2 checkpoint: ref=shared-ref ")
        )
        errors = validate_report_text(
            with_duplicate_ref,
            enforce_checkpoint_target_ref_uniqueness=True,
        )
        self.assertTrue(any("target ref uniqueness" in e for e in errors))

    def test_validate_report_allows_duplicate_target_ref_tokens_within_same_checkpoint(self) -> None:
        with_repeated_same_ref = VALID_REPORT.replace(
            "- F1 checkpoint:",
            "- F1 checkpoint: ref=f1-login ref=f1-login ",
        )
        errors = validate_report_text(
            with_repeated_same_ref,
            enforce_checkpoint_target_ref_uniqueness=True,
        )
        self.assertFalse(any("target ref uniqueness" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_target_refs_are_unique(self) -> None:
        with_refs = (
            VALID_REPORT.replace("- F1 checkpoint:", "- F1 checkpoint: ref=f1-login ")
            .replace("- F2 checkpoint:", "- F2 checkpoint: ref=f2-error ")
            .replace("- F3 checkpoint:", "- F3 checkpoint: ref=f3-required ")
            .replace("- F4 checkpoint:", "- F4 checkpoint: ref=f4-enter ")
            .replace("- F5 checkpoint:", "- F5 checkpoint: ref=f5-logout ")
            .replace("- V1 checkpoint:", "- V1 checkpoint: ref=v1-layout ")
            .replace("- V2 checkpoint:", "- V2 checkpoint: ref=v2-error ")
            .replace("- V3 checkpoint:", "- V3 checkpoint: ref=v3-dashboard ")
            .replace("- O1 checkpoint:", "- O1 checkpoint: ref=o1-wrong-password ")
            .replace("- O2 checkpoint:", "- O2 checkpoint: ref=o2-empty-password ")
        )
        self.assertEqual(
            validate_report_text(
                with_refs,
                enforce_checkpoint_target_ref_uniqueness=True,
            ),
            [],
        )

    def test_validate_report_fails_when_checkpoint_artifact_refs_are_not_unique(self) -> None:
        with_duplicate_artifact = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible `artifacts/shared.log`",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert `artifacts/shared.log`",
        )
        errors = validate_report_text(
            with_duplicate_artifact,
            enforce_checkpoint_artifact_ref_uniqueness=True,
        )
        self.assertTrue(any("artifact ref uniqueness" in e for e in errors))

    def test_validate_report_passes_when_checkpoint_artifact_refs_are_unique(self) -> None:
        with_unique_artifacts = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible `artifacts/f1.log`",
        ).replace(
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
            "- F2 checkpoint: Inline error panel rendered and focus moved to form alert `artifacts/f2.log`",
        )
        errors = validate_report_text(
            with_unique_artifacts,
            enforce_checkpoint_artifact_ref_uniqueness=True,
        )
        self.assertFalse(any("artifact ref uniqueness" in e for e in errors))

    def test_validate_report_fails_when_failure_evidence_has_no_artifact_path(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Evidence: `artifacts/f2-failure.png`\n",
            "    - Evidence: screenshot captured in runbook\n",
        )
        errors = validate_report_text(
            broken,
            require_failure_evidence_artifact_paths=True,
        )
        self.assertTrue(any("failure evidence artifact paths" in e for e in errors))

    def test_validate_report_passes_when_failure_evidence_has_artifact_path(self) -> None:
        self.assertEqual(
            validate_report_text(
                FAILED_REPORT_WITH_RECOVERY,
                require_failure_evidence_artifact_paths=True,
            ),
            [],
        )

    def test_validate_report_fails_when_failure_recovery_plan_missing(self) -> None:
        errors = validate_report_text(
            FAILED_REPORT_WITH_RECOVERY,
            require_failure_recovery_plan=True,
        )
        self.assertTrue(any("failure recovery plan" in e for e in errors))

    def test_validate_report_passes_when_failure_recovery_plan_present(self) -> None:
        with_recovery_plan = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Evidence: `artifacts/f2-failure.png`\n",
            "    - Evidence: `artifacts/f2-failure.png`\n"
            "    - Recovery plan: Re-run with deterministic selector fallback, then capture trace and screenshot for triage\n",
        )
        self.assertEqual(
            validate_report_text(
                with_recovery_plan,
                require_failure_recovery_plan=True,
            ),
            [],
        )

    def test_validate_report_fails_when_failure_recovery_owner_missing(self) -> None:
        with_recovery_plan = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Evidence: `artifacts/f2-failure.png`\n",
            "    - Evidence: `artifacts/f2-failure.png`\n"
            "    - Recovery plan: Re-run with deterministic selector fallback, then capture trace and screenshot for triage\n",
        )
        errors = validate_report_text(
            with_recovery_plan,
            require_failure_recovery_owner=True,
        )
        self.assertTrue(any("failure recovery owner" in e for e in errors))

    def test_validate_report_passes_when_failure_recovery_owner_present(self) -> None:
        with_recovery_owner = FAILED_REPORT_WITH_RECOVERY.replace(
            "    - Evidence: `artifacts/f2-failure.png`\n",
            "    - Evidence: `artifacts/f2-failure.png`\n"
            "    - Recovery plan: Re-run with deterministic selector fallback, then capture trace and screenshot for triage\n"
            "    - Recovery owner: qa-oncall@example.test\n",
        )
        self.assertEqual(
            validate_report_text(
                with_recovery_owner,
                require_failure_recovery_owner=True,
            ),
            [],
        )

    def test_validate_report_fails_when_failed_check_checkpoint_is_not_fail(self) -> None:
        broken = FAILED_REPORT_WITH_RECOVERY.replace(
            "- F2 checkpoint: FAIL - Inline error panel missing after submit",
            "- F2 checkpoint: PASS - Inline error panel missing after submit",
        )
        errors = validate_report_text(broken, strict=True)
        self.assertTrue(any("failed checks must map to execution-log checkpoints marked FAIL" in e for e in errors))

    def test_validate_report_passes_when_failure_summary_is_zero_with_no_failed_checks(self) -> None:
        with_breakdown = VALID_REPORT.replace(
            "- Merge recommendation: **APPROVE**\n",
            "- Merge recommendation: **APPROVE**\n"
            "- Failure breakdown: selector=0, runtime=0, product=0\n",
        )
        self.assertEqual(
            validate_report_text(
                with_breakdown,
                require_failure_classification_summary=True,
            ),
            [],
        )

    def test_validate_report_fails_when_failed_checkpoint_has_no_artifact_path(self) -> None:
        errors = validate_report_text(
            FAILED_REPORT_WITH_RECOVERY,
            require_failure_checkpoint_artifact_paths=True,
        )
        self.assertTrue(any("failure checkpoint artifact paths" in e for e in errors))

    def test_validate_report_passes_when_failed_checkpoint_has_artifact_path(self) -> None:
        with_checkpoint_artifact = FAILED_REPORT_WITH_RECOVERY.replace(
            "- F2 checkpoint: FAIL - Inline error panel missing after submit",
            "- F2 checkpoint: FAIL - Inline error panel missing after submit `artifacts/f2-checkpoint.log`",
        )
        self.assertEqual(
            validate_report_text(
                with_checkpoint_artifact,
                require_failure_checkpoint_artifact_paths=True,
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()


    def test_validate_report_fails_when_qa_inventory_bullet_has_no_checks_mapping(self) -> None:
        with_inventory = VALID_REPORT.replace(
            "## Scope\n",
            "## 1) QA inventory\n- Claim: Login works for valid user\n\n## Scope\n",
        )
        errors = validate_report_text(with_inventory, require_qa_inventory_check_refs=True)
        self.assertTrue(any("every QA inventory bullet must include 'Checks:' mapping" in e for e in errors))

    def test_validate_report_passes_when_qa_inventory_checks_mapping_is_present(self) -> None:
        with_inventory = VALID_REPORT.replace(
            "## Scope\n",
            "## 1) QA inventory\n- Claim: Login works for valid user -> Checks: F1, F4\n- Claim: Invalid password stays blocked -> Checks: O1, F2\n\n## Scope\n",
        )
        self.assertEqual(
            validate_report_text(with_inventory, require_qa_inventory_check_refs=True),
            [],
        )
