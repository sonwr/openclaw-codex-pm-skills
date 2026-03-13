from pathlib import Path
import unittest


class GovernanceSandboxReportBundleNameAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_report_bundle_name_alias_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_NAME_ALIAS_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_REPORT_BUNDLE_NAME_ALIAS_NOTE.md").exists())
