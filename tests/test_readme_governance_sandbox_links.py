from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxLinkTests(unittest.TestCase):
    def test_readme_keeps_web_demo_form_proof_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_FORM_PROOF.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_FORM_PROOF.md", readme)

    def test_readme_keeps_result_download_check_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_DOWNLOAD_CHECK.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_DOWNLOAD_CHECK.md", readme)

    def test_readme_keeps_scenario_report_alias_expansion_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION.md", readme)

    def test_readme_keeps_stdin_report_bundle_note_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_STDIN_REPORT_BUNDLE_NOTE.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_STDIN_REPORT_BUNDLE_NOTE.md", readme)

    def test_readme_keeps_dao_report_example_note_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_DAO_REPORT_EXAMPLE_NOTE.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_DAO_REPORT_EXAMPLE_NOTE.md", readme)

    def test_readme_keeps_list_presets_note_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_LIST_PRESETS_NOTE.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_LIST_PRESETS_NOTE.md", readme)

    def test_readme_keeps_playwright_recovery_note_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_PLAYWRIGHT_RECOVERY_NOTE.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_PLAYWRIGHT_RECOVERY_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
