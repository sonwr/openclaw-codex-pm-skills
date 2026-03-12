from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioJsonYamlReportStartTest(unittest.TestCase):
    def test_readme_mentions_json_yaml_report_start_note(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/GOVERNANCE_SANDBOX_SCENARIO_JSON_YAML_REPORT_START.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
