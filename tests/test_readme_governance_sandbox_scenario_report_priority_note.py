from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioReportPriorityNoteTest(unittest.TestCase):
    def test_readme_mentions_priority_note(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_NOTE.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
