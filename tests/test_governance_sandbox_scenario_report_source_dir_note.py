from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportSourceDirNoteTests(unittest.TestCase):
    def test_readme_mentions_source_dir_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SOURCE_DIR_NOTE.md", readme)

    def test_note_mentions_scenario_source_and_report_directory(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_SOURCE_DIR_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario source", doc)
        self.assertIn("report directory", doc)


if __name__ == "__main__":
    unittest.main()
