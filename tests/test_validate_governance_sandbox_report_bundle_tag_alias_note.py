from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxReportBundleTagAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_report_bundle_tag_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_BUNDLE_TAG_ALIAS_NOTE.md", readme)

    def test_note_mentions_report_bundle_tag_and_report_bundle(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_BUNDLE_TAG_ALIAS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("report_bundle_tag", doc)
        self.assertIn("JSON, Markdown, and HTML report bundle", doc)


if __name__ == "__main__":
    unittest.main()
