from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioReportReplayGateTest(unittest.TestCase):
    def test_readme_mentions_replay_gate_note(self) -> None:
        readme = Path('README.md').read_text()
        self.assertIn(
            'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_REPLAY_GATE.md',
            readme,
        )


if __name__ == '__main__':
    unittest.main()
