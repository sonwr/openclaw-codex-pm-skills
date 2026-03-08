from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import validate_web_qa_report


VALID_REPORT = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n- Viewport: `1366x768`\n- Test account: `qa.user@example.test`\n\n## 2) Checklist execution summary\n- Functional checks (5/5 pass)\n  - F1: PASS\n  - F2: PASS\n  - F3: PASS\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n- F3 checkpoint: Required-field validation blocked form submit\n- F4 checkpoint: Pressing Enter on password field triggered submit\n- F5 checkpoint: Logout redirected to `/login`\n- V1 checkpoint: Captured baseline layout screenshot\n- V2 checkpoint: Captured error-state screenshot\n- V3 checkpoint: Captured dashboard screenshot\n- O1 checkpoint: Wrong-password path stayed on `/login`\n- O2 checkpoint: Empty-password path showed client-side validation\n\n## 4) Signoff\n- Regressions: 0\n- Merge recommendation: **APPROVE**\n"""


class ValidateWebQaReportCliTests(unittest.TestCase):
    def test_cli_json_output_for_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(report_path),
                    "--strict",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "PASS")
            self.assertTrue(payload["strict"])
            self.assertFalse(payload["require_checkpoint_timestamps"])
            self.assertFalse(payload["enforce_monotonic_checkpoint_timestamps"])
            self.assertEqual(payload["counts"]["functional"], 5)

    def test_cli_writes_json_payload_to_file_when_json_out_is_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            json_path = Path(tmpdir) / "artifacts" / "validation.json"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(report_path),
                    "--strict",
                    "--json-out",
                    str(json_path),
                ],
            ):
                validate_web_qa_report.main()

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "PASS")
            self.assertTrue(payload["strict"])
            self.assertEqual(payload["file"], str(report_path))

    def test_cli_json_output_with_playwright_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--playwright-interactive-profile",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["playwright_interactive_profile"])
            self.assertTrue(payload["strict"])
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(payload["require_failure_recovery_plan"])
            self.assertTrue(payload["require_failure_recovery_owner"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_json_output_with_deterministic_replay_profile_alias(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--deterministic-replay-profile",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["deterministic_replay_profile"])
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_json_output_with_strict_replay_profile_alias(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--strict-replay-profile",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["strict_replay_profile"])
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_json_output_for_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            broken = VALID_REPORT.replace("  - V2: PASS `shots/v2.png`", "  - V2: PASS")
            report_path.write_text(broken, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--strict",
                        "--json",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["errors"])
            self.assertEqual(payload["error_count"], len(payload["errors"]))

    def test_cli_json_output_for_checkpoint_timestamp_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-checkpoint-timestamps",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_json_output_for_monotonic_checkpoint_timestamp_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--enforce-monotonic-checkpoint-timestamps",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["enforce_monotonic_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamp order" in err for err in payload["errors"]))

    def test_cli_json_output_for_visual_checkpoint_evidence_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-visual-checkpoint-evidence",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_visual_checkpoint_evidence"])
            self.assertTrue(any("visual checkpoint evidence" in err for err in payload["errors"]))

    def test_cli_json_output_for_checkpoint_status_token_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--enforce-checkpoint-status-tokens",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["enforce_checkpoint_status_tokens"])
            self.assertTrue(any("checkpoint status tokens" in err for err in payload["errors"]))

    def test_cli_json_output_for_checkpoint_check_status_consistency_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--enforce-checkpoint-to-check-status-consistency",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["enforce_checkpoint_to_check_status_consistency"])
            self.assertTrue(any("status consistency" in err for err in payload["errors"]))

    def test_cli_json_output_for_checkpoint_artifact_path_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-checkpoint-artifact-paths",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_checkpoint_artifact_paths"])
            self.assertTrue(any("checkpoint artifact paths" in err for err in payload["errors"]))

    def test_cli_stdout_reports_checkpoint_artifact_path_check_when_enabled(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
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
            report_path.write_text(with_artifacts, encoding="utf-8")

            output = io.StringIO()
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(report_path),
                    "--require-checkpoint-artifact-paths",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()

            text = output.getvalue()
            self.assertIn("web-qa-playwright report validation: PASS", text)
            self.assertIn("- checkpoint artifact path checks: enabled", text)

    def test_cli_json_output_for_checkpoint_target_ref_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-checkpoint-target-refs",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_checkpoint_target_refs"])
            self.assertTrue(any("checkpoint target refs" in err for err in payload["errors"]))

    def test_cli_json_output_for_checkpoint_artifact_ref_uniqueness_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            duplicate_artifact_report = VALID_REPORT.replace(
                "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
                "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible `artifacts/shared.log`",
            ).replace(
                "- F2 checkpoint: Inline error panel rendered and focus moved to form alert",
                "- F2 checkpoint: Inline error panel rendered and focus moved to form alert `artifacts/shared.log`",
            )
            report_path.write_text(duplicate_artifact_report, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--enforce-checkpoint-artifact-ref-uniqueness",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["enforce_checkpoint_artifact_ref_uniqueness"])
            self.assertTrue(any("artifact ref uniqueness" in err for err in payload["errors"]))

    def test_cli_json_output_for_failure_recovery_plan_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            failed_report = VALID_REPORT.replace(
                "  - F2: PASS",
                "  - F2: FAIL\n"
                "    - Expected: Login success toast appears within 2 seconds\n"
                "    - Observed: Spinner persisted for 10 seconds\n"
                "    - First failure timestamp: 2026-03-07T04:10:00Z\n"
                "    - Retry: FAIL\n"
                "    - Failure classification: product\n"
                "    - Evidence: `artifacts/f2-failure.png`",
            ).replace("- Regressions: 0", "- Regressions: 1").replace(
                "- Merge recommendation: **APPROVE**",
                "- Merge recommendation: **BLOCK**",
            )
            report_path.write_text(failed_report, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-failure-recovery-plan",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_failure_recovery_plan"])
            self.assertTrue(any("failure recovery plan" in err for err in payload["errors"]))

    def test_cli_json_output_for_failure_classification_summary_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            failed_report = VALID_REPORT.replace(
                "  - F2: PASS",
                "  - F2: FAIL\n"
                "    - Expected: Login success toast appears within 2 seconds\n"
                "    - Observed: Spinner persisted for 10 seconds\n"
                "    - First failure timestamp: 2026-03-07T04:10:00Z\n"
                "    - Retry: FAIL\n"
                "    - Failure classification: product\n"
                "    - Evidence: `artifacts/f2-failure.png`",
            ).replace("- Regressions: 0", "- Regressions: 1").replace(
                "- Merge recommendation: **APPROVE**",
                "- Merge recommendation: **BLOCK**",
            )
            report_path.write_text(failed_report, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-failure-classification-summary",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_failure_classification_summary"])
            self.assertTrue(any("failure classification summary" in err for err in payload["errors"]))

    def test_cli_json_output_for_execution_log_step_count_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            broken = VALID_REPORT.replace(
                "- O2 checkpoint: Empty-password path showed client-side validation\n",
                "- O2 checkpoint: Empty-password path showed client-side validation\n"
                "- Notes: extra line for humans\n",
            )
            report_path.write_text(broken, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-execution-log-step-count-match",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_execution_log_step_count_match"])
            self.assertTrue(any("execution log step count" in err for err in payload["errors"]))

    def test_cli_strict_plus_enables_reproducibility_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--strict-plus",
                        "--json",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["strict"])
            self.assertTrue(payload["strict_plus"])
            self.assertTrue(payload["enforce_checkpoint_format"])
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(payload["enforce_monotonic_checkpoint_timestamps"])
            self.assertTrue(payload["enforce_checkpoint_status_tokens"])
            self.assertTrue(payload["require_visual_checkpoint_evidence"])
            self.assertTrue(payload["require_checkpoint_artifact_paths"])
            self.assertTrue(payload["require_checkpoint_target_refs"])
            self.assertTrue(payload["require_failure_checkpoint_artifact_paths"])
            self.assertTrue(payload["require_failure_evidence_artifact_paths"])
            self.assertTrue(payload["require_failure_recovery_plan"])
            self.assertTrue(payload["enforce_checkpoint_to_check_status_consistency"])
            self.assertTrue(payload["require_failure_classification_summary"])
            self.assertTrue(payload["require_execution_log_step_count_match"])
            self.assertTrue(payload["require_qa_inventory_section"])

    def test_cli_json_output_for_qa_inventory_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(VALID_REPORT, encoding="utf-8")

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--json",
                        "--require-qa-inventory-section",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_qa_inventory_section"])
            self.assertTrue(any("qa inventory" in err for err in payload["errors"]))

    def test_cli_strict_plus_combined_fail_fixture_surfaces_multiple_repro_errors(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_plus_combined_fail.md"
        )
        output = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(fixture_path),
                    "--strict-plus",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()
        self.assertEqual(exc.exception.code, 1)

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "FAIL")
        self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))
        self.assertTrue(any("failure classification" in err for err in payload["errors"]))
        self.assertTrue(any("execution log step count" in err for err in payload["errors"]))

    def test_cli_strict_plus_pass_fixture_satisfies_replay_gates(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_plus_pass.md"
        )
        output = io.StringIO()

        with mock.patch(
            "sys.argv",
            [
                "validate_web_qa_report.py",
                "--file",
                str(fixture_path),
                "--strict-plus",
                "--json",
            ],
        ):
            with contextlib.redirect_stdout(output):
                validate_web_qa_report.main()

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "PASS")
        self.assertNotIn("errors", payload)
        self.assertTrue(payload["strict_plus"])

    def test_cli_strict_plus_monotonic_timestamp_only_fixture_isolates_replay_order_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_monotonic_timestamp_only.md"
        )
        output = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(fixture_path),
                    "--strict-plus",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()
        self.assertEqual(exc.exception.code, 1)

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "FAIL")
        self.assertEqual(payload["error_count"], 1)
        self.assertIn("checkpoint timestamp order", payload["errors"][0])
        self.assertNotIn("artifact ref", "\n".join(payload["errors"]))
        self.assertNotIn("failure classification", "\n".join(payload["errors"]))

    def test_cli_strict_plus_artifact_ref_reuse_only_fixture_isolates_single_repro_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_artifact_ref_reuse_only.md"
        )
        output = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(fixture_path),
                    "--strict-plus",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()
        self.assertEqual(exc.exception.code, 1)

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "FAIL")
        self.assertEqual(payload["error_count"], 1)
        self.assertIn("artifact ref", payload["errors"][0])
        self.assertNotIn("checkpoint timestamps", "\n".join(payload["errors"]))
        self.assertNotIn("failure classification", "\n".join(payload["errors"]))

    def test_cli_strict_plus_status_inconsistency_only_fixture_isolates_single_repro_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_status_inconsistency_only.md"
        )
        output = io.StringIO()

        with self.assertRaises(SystemExit) as exc:
            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(fixture_path),
                    "--strict-plus",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()
        self.assertEqual(exc.exception.code, 1)

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "FAIL")
        self.assertEqual(payload["error_count"], 1)
        self.assertIn("status consistency", payload["errors"][0])
        self.assertNotIn("checkpoint timestamp order", "\n".join(payload["errors"]))
        self.assertNotIn("artifact ref", "\n".join(payload["errors"]))

    def test_cli_writes_fail_json_payload_to_json_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            json_path = Path(tmpdir) / "artifacts" / "validation-fail.json"
            broken = VALID_REPORT.replace("  - V2: PASS `shots/v2.png`", "  - V2: PASS")
            report_path.write_text(broken, encoding="utf-8")

            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--strict",
                        "--json-out",
                        str(json_path),
                    ],
                ):
                    validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "FAIL")
            self.assertGreater(payload["error_count"], 0)
            self.assertEqual(payload["file"], str(report_path))


if __name__ == "__main__":
    unittest.main()
