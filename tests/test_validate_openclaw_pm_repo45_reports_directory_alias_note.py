from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45ReportsDirectoryAliasNoteTest(unittest.TestCase):
    def test_readme_mentions_repo45_reports_directory_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_REPORTS_DIRECTORY_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_REPORTS_DIRECTORY_ALIAS_NOTE.md").exists())
