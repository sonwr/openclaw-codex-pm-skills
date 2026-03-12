from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioFileFirstRuleTest(unittest.TestCase):
    def test_readme_mentions_scenario_file_first_rule(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_FIRST_RULE.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
