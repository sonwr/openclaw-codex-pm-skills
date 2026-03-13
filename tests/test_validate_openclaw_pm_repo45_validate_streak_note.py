from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidateOpenClawPmRepo45ValidateStreakNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_validate_streak_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_VALIDATE_STREAK_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_VALIDATE_STREAK_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
