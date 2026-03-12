from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeReportHeadlineAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_report_headline_alias_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_HEADLINE_ALIAS_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_REPORT_HEADLINE_ALIAS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
