import unittest
from pathlib import Path


class ReadmeGovernanceSandboxScenarioFileReportPhaseOneStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_file_report_phase_one_status_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_PHASE_ONE_STATUS_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
