from pathlib import Path
import unittest

README = Path(__file__).resolve().parents[1] / 'README.md'


class ReadmeRepo45ReportsDirectoryValidateStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_reports_directory_validate_status_note(self) -> None:
        text = README.read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORTS_DIRECTORY_VALIDATE_STATUS_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
