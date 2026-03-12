from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxMinimumWinStatusNoteTest(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_MINIMUM_WIN_STATUS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_MINIMUM_WIN_STATUS_NOTE.md").exists())

    def test_note_keeps_scenario_and_report_first(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_MINIMUM_WIN_STATUS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario file import", note)
        self.assertIn("report artifact lane", note)
        self.assertIn("validation command", note)


if __name__ == "__main__":
    unittest.main()
