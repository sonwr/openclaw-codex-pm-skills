import unittest
from pathlib import Path


class ReadmeOpenclawPmRepo45ScenarioReportValidateStreakNoteTests(unittest.TestCase):
    def test_readme_mentions_validate_streak_note(self) -> None:
        text = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_SCENARIO_REPORT_VALIDATE_STREAK_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
