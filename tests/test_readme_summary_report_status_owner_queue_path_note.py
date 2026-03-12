from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeSummaryReportStatusOwnerQueuePathNoteTests(unittest.TestCase):
    def test_readme_mentions_summary_report_status_owner_queue_path_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/CLI_SUMMARY_REPORT_STATUS_OWNER_QUEUE_PATH_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'CLI_SUMMARY_REPORT_STATUS_OWNER_QUEUE_PATH_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
