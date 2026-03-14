import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')


class ReadmeGovernanceSandboxScenarioFileReportUiPlaywrightGateTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_file_report_ui_playwright_gate(self) -> None:
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_UI_PLAYWRIGHT_GATE.md', README)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_UI_PLAYWRIGHT_GATE.md').exists())


if __name__ == '__main__':
    unittest.main()
