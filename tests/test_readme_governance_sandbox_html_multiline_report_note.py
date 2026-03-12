from pathlib import Path
import unittest


class ReadmeGovernanceSandboxHtmlMultilineReportNoteTests(unittest.TestCase):
    def test_readme_mentions_html_multiline_report_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_HTML_MULTILINE_REPORT_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_HTML_MULTILINE_REPORT_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
