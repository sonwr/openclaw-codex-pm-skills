from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeOpenclawPmRepo45SourcePathAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_openclaw_pm_repo45_source_path_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_SOURCE_PATH_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_SOURCE_PATH_ALIAS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
