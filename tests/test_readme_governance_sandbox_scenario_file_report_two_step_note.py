from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioFileReportTwoStepNoteTests(unittest.TestCase):
    def test_readme_mentions_two_step_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_TWO_STEP_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_TWO_STEP_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
