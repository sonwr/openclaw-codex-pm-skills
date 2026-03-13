import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')

class ReadmeGovernanceSandboxScenarioJsonYamlReportStartTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_json_yaml_report_start(self) -> None:
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_JSON_YAML_REPORT_START.md', README)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_JSON_YAML_REPORT_START.md').exists())

if __name__ == '__main__':
    unittest.main()
