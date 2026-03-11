from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioReportPriorityLaneTest(unittest.TestCase):
    def test_readme_mentions_priority_lane_note(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_LANE.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
