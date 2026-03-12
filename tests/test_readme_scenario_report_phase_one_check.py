from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeScenarioReportPhaseOneCheckTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_phase_one_check(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_CHECK.md', readme)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_CHECK.md').exists())


if __name__ == '__main__':
    unittest.main()
