from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioSourceBasenameNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_source_basename_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_BASENAME_NOTE.md", readme)

    def test_note_mentions_source_path_and_report_basename(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_SOURCE_BASENAME_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario source path", doc)
        self.assertIn("report bundle basename", doc)


if __name__ == "__main__":
    unittest.main()
