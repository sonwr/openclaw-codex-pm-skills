from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportMetadataCardTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_report_metadata_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_METADATA_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_METADATA_CARD.md").exists())

    def test_note_keeps_metadata_card_scope_small(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_METADATA_CARD.md").read_text(encoding="utf-8")

        self.assertIn("generated-at timestamp", note)
        self.assertIn("scenario source path", note)
        self.assertIn("JSON/Markdown/HTML artifact paths", note)


if __name__ == "__main__":
    unittest.main()
