from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReadmeOpenclawPmRepo45ReportOutputBasenameAliasNoteTest(unittest.TestCase):
    def test_readme_mentions_report_output_basename_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_BASENAME_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_REPORT_OUTPUT_BASENAME_ALIAS_NOTE.md").exists())

if __name__ == "__main__":
    unittest.main()
