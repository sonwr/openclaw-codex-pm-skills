from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxRepo45ScenarioReportFirstNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_report_first_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_REPO45_SCENARIO_REPORT_FIRST_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_REPO45_SCENARIO_REPORT_FIRST_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
