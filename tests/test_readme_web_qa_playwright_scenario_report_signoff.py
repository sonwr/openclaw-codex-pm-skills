import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaPlaywrightScenarioReportSignoffTest(unittest.TestCase):
    def test_readme_mentions_web_qa_playwright_scenario_report_signoff(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/WEB_QA_PLAYWRIGHT_SCENARIO_REPORT_SIGNOFF.md', readme)
        self.assertTrue((ROOT / 'docs' / 'WEB_QA_PLAYWRIGHT_SCENARIO_REPORT_SIGNOFF.md').exists())


if __name__ == '__main__':
    unittest.main()
