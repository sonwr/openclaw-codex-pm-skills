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


VALID_REPORT = """# Sample\n\n## Scope\n- URL: `https://example.test/login`\n- Viewport: `1366x768`\n- Test account: `qa.user@example.test`\n\n## 2) Checklist execution summary\n- Functional checks (5/5 pass)\n  - F1: PASS\n  - F2: PASS\n  - F3: PASS\n  - F4: PASS\n  - F5: PASS\n- Visual checks (3/3 pass)\n  - V1: PASS `shots/v1.png`\n  - V2: PASS `shots/v2.png`\n  - V3: PASS `shots/v3.png`\n- Off-happy-path checks (2/2 pass)\n  - O1: PASS\n  - O2: PASS\n\n## 3) Execution log\n- F1 checkpoint: URL changed to `/dashboard`, user avatar visible\n- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n- F3 checkpoint: Required-field validation blocked form submit\n- F4 checkpoint: Pressing Enter on password field triggered submit\n- F5 checkpoint: Logout redirected to `/login`\n- V1 checkpoint: Captured baseline layout screenshot\n- V2 checkpoint: Captured error-state screenshot\n- V3 checkpoint: Captured dashboard screenshot\n- O1 checkpoint: Wrong-password path stayed on `/login`\n- O2 checkpoint: Empty-password path showed client-side validation\n\n## 4) Signoff\n- Regressions: 0\n- Merge recommendation: **APPROVE**\n- Replay readiness: **READY**\n- Next action: Archive artifacts and proceed to release signoff\n"""


class ValidateWebQaReportCliTests(unittest.TestCase):

    def test_cli_json_output_exposes_checkpoint_ref_metadata_for_replay_triage(self) -> None:
        report = VALID_REPORT.replace(
            "- F1 checkpoint: URL changed to `/dashboard`, user avatar visible",
            "- F1 checkpoint: PASS 2026-03-08T14:40:00Z ref=e12 URL changed to `/dashboard`, artifact `artifacts/f1.png` user avatar visible",
        ).replace(
            "- V1 checkpoint: Captured baseline layout screenshot",
            "- V1 checkpoint: PASS 2026-03-08T14:41:00Z ref=e44 Captured baseline layout screenshot `artifacts/v1.png`",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(report, encoding="utf-8")

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
            self.assertEqual(payload["report_metadata"]["checkpoint_order"][:2], ["F1", "F2"])
            self.assertEqual(payload["report_metadata"]["checkpoint_count"], 10)
            self.assertEqual(payload["report_metadata"]["missing_checkpoint_ids"], [])
            self.assertEqual(payload["report_metadata"]["unexpected_checkpoint_ids"], [])
            self.assertEqual(payload["report_metadata"]["checkpoint_target_refs"], ["e12", "e44"])
            self.assertEqual(payload["report_metadata"]["checkpoint_target_ref_id_count"], 2)
            self.assertEqual(payload["report_metadata"]["checkpoint_target_refs_by_id"]["F1"], ["e12"])
            self.assertEqual(payload["report_metadata"]["checkpoint_artifact_refs"], ["artifacts/f1.png", "artifacts/v1.png"])
            self.assertEqual(payload["report_metadata"]["checkpoint_artifact_ref_id_count"], 2)
            self.assertEqual(payload["report_metadata"]["checkpoint_artifact_refs_by_id"]["V1"], ["artifacts/v1.png"])
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
            self.assertEqual(payload["validation_schema_version"], 1)
            self.assertFalse(payload["require_replay_readiness"])
            self.assertTrue(payload["strict"])
            self.assertFalse(payload["require_checkpoint_timestamps"])
            self.assertFalse(payload["enforce_monotonic_checkpoint_timestamps"])
            self.assertEqual(payload["counts"]["functional"], 5)
            self.assertIsNone(payload["active_profile_preset"])

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
            self.assertEqual(payload["validation_schema_version"], 1)
            self.assertTrue(payload["playwright_interactive_profile"])
            self.assertEqual(payload["active_profile_preset"], "playwright-interactive-profile")
            self.assertTrue(payload["strict"])
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(payload["require_failure_recovery_plan"])
            self.assertFalse(payload["require_qa_inventory_check_refs"])
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
            self.assertEqual(payload["active_profile_preset"], "deterministic-replay-profile")
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
            self.assertEqual(payload["active_profile_preset"], "strict-replay-profile")
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_json_output_with_ci_replay_profile_alias(self) -> None:
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
                        "--ci-replay-profile",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["ci_replay_profile"])
            self.assertEqual(payload["active_profile_preset"], "ci-replay-profile")
            self.assertTrue(payload["require_checkpoint_timestamps"])
            self.assertTrue(any("checkpoint timestamps" in err for err in payload["errors"]))

    def test_cli_strict_plus_check_ref_pass_fixture_satisfies_opt_in_mapping_rule(self) -> None:
        root = Path(__file__).resolve().parents[1]
        report_path = root / "examples" / "web_qa_playwright_strict_plus_with_check_refs_pass.md"

        output = io.StringIO()
        with mock.patch(
            "sys.argv",
            [
                "validate_web_qa_report.py",
                "--file",
                str(report_path),
                "--strict-plus",
                "--require-qa-inventory-check-refs",
                "--json",
            ],
        ):
            with contextlib.redirect_stdout(output):
                validate_web_qa_report.main()

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "PASS")
        self.assertTrue(payload["require_qa_inventory_check_refs"])
        self.assertEqual(
            payload["report_metadata"]["qa_inventory_check_refs"],
            ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"],
        )
        self.assertEqual(payload["report_metadata"]["unresolved_failed_check_ids"], [])
        self.assertEqual(payload["report_metadata"]["unresolved_failed_check_count"], 0)

    def test_cli_json_out_with_strict_plus_check_ref_pass_fixture_writes_metadata_file(self) -> None:
        root = Path(__file__).resolve().parents[1]
        report_path = root / "examples" / "web_qa_playwright_strict_plus_with_check_refs_pass.md"

        with tempfile.TemporaryDirectory() as tmpdir:
            json_path = Path(tmpdir) / "artifacts" / "strict-plus.validation.json"

            with mock.patch(
                "sys.argv",
                [
                    "validate_web_qa_report.py",
                    "--file",
                    str(report_path),
                    "--strict-plus",
                    "--require-qa-inventory-check-refs",
                    "--json-out",
                    str(json_path),
                ],
            ):
                validate_web_qa_report.main()

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "PASS")
            self.assertTrue(payload["strict_plus"])
            self.assertTrue(payload["require_qa_inventory_check_refs"])
            self.assertEqual(payload["active_profile_preset"], "strict-plus")
            self.assertEqual(payload["counts"]["functional"], 5)
            self.assertEqual(payload["counts"]["visual"], 3)
            self.assertEqual(payload["counts"]["off_happy"], 2)
            self.assertEqual(
                payload["report_metadata"]["qa_inventory_check_refs"],
                ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"],
            )

    def test_cli_json_output_with_explicit_qa_inventory_check_refs_requirement(self) -> None:
        root = Path(__file__).resolve().parents[1]
        report_path = root / "examples" / "web_qa_playwright_strict_plus_pass.md"

        output = io.StringIO()
        with mock.patch(
            "sys.argv",
            [
                "validate_web_qa_report.py",
                "--file",
                str(report_path),
                "--strict-plus",
                "--require-qa-inventory-check-refs",
                "--json",
            ],
        ):
            with contextlib.redirect_stdout(output):
                validate_web_qa_report.main()

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "PASS")
        self.assertTrue(payload["require_qa_inventory_check_refs"])


    def test_cli_json_output_requires_full_qa_inventory_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(
                VALID_REPORT.replace(
                    "## 3) Execution log",
                    "## 1) QA inventory\n- Browser/runtime: Playwright Chromium (headless) | Checks: F1, F2, F3, F4, F5, V1, V2, V3, O1\n\n## 3) Execution log",
                ),
                encoding="utf-8",
            )

            output = io.StringIO()
            with self.assertRaises(SystemExit) as exc:
                with mock.patch(
                    "sys.argv",
                    [
                        "validate_web_qa_report.py",
                        "--file",
                        str(report_path),
                        "--require-qa-inventory-check-refs",
                        "--require-qa-inventory-full-coverage",
                        "--json",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)

            payload = json.loads(output.getvalue().strip())
            self.assertEqual(payload["status"], "FAIL")
            self.assertTrue(payload["require_qa_inventory_full_coverage"])
            self.assertTrue(any("missing: O2" in err for err in payload["errors"]))

    def test_cli_json_output_strict_plus_sets_active_profile_preset(self) -> None:
        root = Path(__file__).resolve().parents[1]
        report_path = root / "examples" / "web_qa_playwright_strict_plus_pass.md"

        output = io.StringIO()
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

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["active_profile_preset"], "strict-plus")

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

    def test_cli_stdout_reports_qa_inventory_full_coverage_check_when_enabled(self) -> None:
        root = Path(__file__).resolve().parents[1]
        report_path = root / "examples" / "web_qa_playwright_strict_plus_pass.md"

        output = io.StringIO()
        with mock.patch(
            "sys.argv",
            [
                "validate_web_qa_report.py",
                "--file",
                str(report_path),
                "--strict-plus",
                "--require-qa-inventory-check-refs",
                "--require-qa-inventory-full-coverage",
            ],
        ):
            with contextlib.redirect_stdout(output):
                validate_web_qa_report.main()

        text = output.getvalue()
        self.assertIn("web-qa-playwright report validation: PASS", text)
        self.assertIn("- qa inventory full-coverage checks: enabled", text)

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

    def test_cli_stdout_reports_next_action_gates_when_enabled(self) -> None:
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
                    "--require-next-action",
                    "--require-next-action-failed-check-ref",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()

            text = output.getvalue()
            self.assertIn("web-qa-playwright report validation: PASS", text)
            self.assertIn("- next action handoff checks: enabled", text)
            self.assertIn("- next action failed-check traceability checks: enabled", text)

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

    def test_cli_strict_plus_target_ref_reuse_only_fixture_isolates_single_traceability_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_target_ref_reuse_only.md"
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
                    "--enforce-checkpoint-target-ref-uniqueness",
                    "--json",
                ],
            ):
                with contextlib.redirect_stdout(output):
                    validate_web_qa_report.main()
        self.assertEqual(exc.exception.code, 1)

        payload = json.loads(output.getvalue().strip())
        self.assertEqual(payload["status"], "FAIL")
        self.assertEqual(payload["error_count"], 1)
        self.assertIn("target ref uniqueness", payload["errors"][0])
        self.assertNotIn("checkpoint artifact paths", "\n".join(payload["errors"]))

    def test_cli_strict_plus_missing_artifact_paths_only_fixture_isolates_single_repro_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_artifact_paths_only.md"
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
        self.assertIn("checkpoint artifact paths", payload["errors"][0])
        self.assertNotIn("artifact ref", "\n".join(payload["errors"]))
        self.assertNotIn("target refs", "\n".join(payload["errors"]))

    def test_cli_strict_plus_missing_target_refs_fixture_isolates_single_traceability_error(self) -> None:
        fixture_path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "web_qa_playwright_strict_fail_missing_target_refs.md"
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
        self.assertIn("checkpoint target refs", payload["errors"][0])
        self.assertNotIn("artifact ref", "\n".join(payload["errors"]))
        self.assertNotIn("checkpoint artifact paths", "\n".join(payload["errors"]))

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

    def test_cli_json_output_for_explicit_replay_readiness_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            broken = VALID_REPORT.replace("- Replay readiness: **READY**\n", "")
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
                        "--require-replay-readiness",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)
            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_replay_readiness"])
            self.assertTrue(any("Replay readiness" in err for err in payload["errors"]))

    def test_cli_json_output_for_explicit_next_action_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            broken = VALID_REPORT.replace("- Next action: Archive artifacts and proceed to release signoff\n", "")
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
                        "--require-next-action",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)
            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_next_action"])
            self.assertTrue(any("next action" in err.lower() for err in payload["errors"]))

    def test_cli_json_output_requires_failed_check_id_in_next_action(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            broken = VALID_REPORT.replace(
                "- F2: PASS\n",
                "- F2: FAIL\n"
                "    - Expected: Login success toast appears within 2 seconds\n"
                "    - Observed: Spinner persisted for 10 seconds\n"
                "    - First failure timestamp: 2026-03-07T04:10:00Z\n"
                "    - Retry: FAIL\n"
                "    - Failure classification: product\n"
                "    - Evidence: `artifacts/f2-failure.png`\n",
            ).replace(
                "- Functional checks (5/5 pass)",
                "- Functional checks (4/5 pass)",
            ).replace(
                "- F2 checkpoint: Inline error panel rendered and focus moved to form alert\n",
                "- F2 checkpoint: FAIL - Inline error panel missing after submit\n",
            ).replace(
                "- Regressions: 0\n",
                "- Regressions: 1\n",
            ).replace(
                "- Merge recommendation: **APPROVE**\n",
                "- Merge recommendation: **BLOCK**\n",
            ).replace(
                "- Replay readiness: **READY**\n",
                "- Replay readiness: **BLOCKED**\n",
            ).replace(
                "- Next action: Archive artifacts and proceed to release signoff\n",
                "- Next action: Investigate spinner timeout and rerun login flow\n",
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
                        "--require-next-action",
                        "--require-next-action-failed-check-ref",
                    ],
                ):
                    with contextlib.redirect_stdout(output):
                        validate_web_qa_report.main()
            self.assertEqual(exc.exception.code, 1)
            payload = json.loads(output.getvalue().strip())
            self.assertTrue(payload["require_next_action_failed_check_ref"])
            self.assertTrue(any("failed check id" in err.lower() for err in payload["errors"]))


if __name__ == "__main__":
    unittest.main()


    def test_cli_json_includes_report_metadata_for_failed_next_action_refs(self) -> None:
        report = self._write_temp_report(
            """# Web QA Report

## 1) QA inventory
- Claim: Checkout blocks invalid coupon codes. Checks: F1
- Functional checks (4 / 5 pass)
  - F1: FAIL - Invalid coupon is accepted
    - Failure classification: product
    - Failure evidence: coupon error missing
  - F2: PASS - Cart subtotal is visible
  - F3: PASS - Shipping estimate is visible
  - F4: PASS - CTA remains enabled
  - F5: PASS - Success banner appears
- Visual checks (3 / 3 pass)
  - V1: PASS - Modal spacing is stable
  - V2: PASS - Error copy aligns with field
  - V3: PASS - Summary card stays within viewport
- Off-happy-path checks (2 / 2 pass)
  - O1: PASS - Empty cart stays blocked
  - O2: PASS - Session timeout returns to login

## 2) Summary
- Regressions: 1
- Failure breakdown: selector=0, runtime=0, product=1

## 3) Execution log
- F1 checkpoint: FAIL ref=e12 `artifacts/f1-fail.png` 2026-03-08T13:00:00Z
- F2 checkpoint: PASS ref=e13 `artifacts/f2-pass.png` 2026-03-08T13:01:00Z
- F3 checkpoint: PASS ref=e14 `artifacts/f3-pass.png` 2026-03-08T13:02:00Z
- F4 checkpoint: PASS ref=e15 `artifacts/f4-pass.png` 2026-03-08T13:03:00Z
- F5 checkpoint: PASS ref=e16 `artifacts/f5-pass.png` 2026-03-08T13:04:00Z
- V1 checkpoint: PASS ref=e17 `artifacts/v1-pass.png` 2026-03-08T13:05:00Z
- V2 checkpoint: PASS ref=e18 `artifacts/v2-pass.png` 2026-03-08T13:06:00Z
- V3 checkpoint: PASS ref=e19 `artifacts/v3-pass.png` 2026-03-08T13:07:00Z
- O1 checkpoint: PASS ref=e20 `artifacts/o1-pass.png` 2026-03-08T13:08:00Z
- O2 checkpoint: PASS ref=e21 `artifacts/o2-pass.png` 2026-03-08T13:09:00Z

## 4) Signoff
- Merge recommendation: BLOCK
- Replay readiness: BLOCKED
- Next action: Fix checkout coupon validation and rerun F1 with a new screenshot.
"""
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--file",
                str(report),
                "--ci-replay-profile",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 1)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["report_metadata"]["failed_check_ids"], ["F1"])
        self.assertEqual(payload["report_metadata"]["failed_check_classifications"], ["product"])
        self.assertEqual(payload["report_metadata"]["failed_check_classifications_by_id"], {"F1": "product"})
        self.assertEqual(payload["report_metadata"]["failed_check_classification_counts"], {"selector": 0, "runtime": 0, "product": 1})
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_ids"], [])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_count"], 0)
        self.assertEqual(payload["report_metadata"]["failed_check_recovery_owners"], {})
        self.assertEqual(payload["report_metadata"]["failed_check_recovery_owner_count"], 0)
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_ids"], ["F1"])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_count"], 1)
        self.assertEqual(payload["report_metadata"]["next_action_failed_check_refs"], ["F1"])
        self.assertEqual(payload["report_metadata"]["failed_check_count"], 1)
        self.assertEqual(payload["report_metadata"]["next_action_failed_check_ref_count"], 1)


    def test_cli_json_tracks_missing_and_present_recovery_owner_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "report.md"
            report_path.write_text(
                FAILED_REPORT_WITH_RECOVERY.replace(
                    "    - Evidence: `artifacts/f2-failure.png`\n",
                    "    - Evidence: `artifacts/f2-failure.png`\n    - Recovery owner: qa-oncall@example.test\n",
                )
                + "- Next action: Investigate F2 spinner timeout and rerun the login flow\n",
                encoding="utf-8",
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    "--file",
                    str(report_path),
                    "--ci-replay-profile",
                    "--json",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(completed.returncode, 0)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["report_metadata"]["failed_check_classifications_by_id"], {"F2": "product"})
        self.assertEqual(payload["report_metadata"]["failed_check_classification_counts"], {"selector": 0, "runtime": 0, "product": 1})
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_ids"], [])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_count"], 0)
        self.assertEqual(
            payload["report_metadata"]["failed_check_recovery_owners"],
            {"F2": "qa-oncall@example.test"},
        )
        self.assertEqual(payload["report_metadata"]["failed_check_recovery_owner_count"], 1)
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_ids"], [])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_count"], 0)

    def test_cli_json_includes_report_metadata_for_pass_report(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--file",
                str(EXAMPLES_DIR / "web_qa_playwright_strict_plus_with_check_refs_pass.md"),
                "--ci-replay-profile",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 0)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["report_metadata"]["failed_check_ids"], [])
        self.assertEqual(payload["report_metadata"]["failed_check_classifications"], [])
        self.assertEqual(payload["report_metadata"]["failed_check_classifications_by_id"], {})
        self.assertEqual(payload["report_metadata"]["failed_check_classification_counts"], {"selector": 0, "runtime": 0, "product": 0})
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_ids"], [])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_classification_count"], 0)
        self.assertEqual(payload["report_metadata"]["failed_check_recovery_owners"], {})
        self.assertEqual(payload["report_metadata"]["failed_check_recovery_owner_count"], 0)
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_ids"], [])
        self.assertEqual(payload["report_metadata"]["missing_failed_check_recovery_owner_count"], 0)
        self.assertEqual(payload["report_metadata"]["next_action_failed_check_refs"], [])
        self.assertEqual(payload["report_metadata"]["failed_check_count"], 0)
