from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenclawPmRepo45ScenarioReportPairNoteTests(unittest.TestCase):
    def test_note_exists_with_phase_one_pair_cues(self) -> None:
        note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_SCENARIO_REPORT_PAIR_NOTE.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("repo 4", note)
        self.assertIn("repo 5", note)
        self.assertIn("scenario file import first", note)
        self.assertIn("markdown/html/json report output coupled", note)
        self.assertIn("docs/OPENCLAW_PM_REPO45_SCENARIO_REPORT_PAIR_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
