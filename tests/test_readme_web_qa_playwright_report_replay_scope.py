from pathlib import Path
import unittest


class ReadmeWebQaPlaywrightReportReplayScopeTest(unittest.TestCase):
    def test_readme_mentions_report_replay_scope(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn('docs/WEB_QA_PLAYWRIGHT_REPORT_REPLAY_SCOPE.md', readme)


if __name__ == '__main__':
    unittest.main()
