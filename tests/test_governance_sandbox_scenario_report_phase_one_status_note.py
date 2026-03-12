from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportPhaseOneStatusNoteTest(unittest.TestCase):
    def test_note_exists_with_phase_one_cues(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_STATUS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario file import stays first", note)
        self.assertIn("markdown/html/json report output stays coupled", note)
        self.assertIn("repos 4 and 5 are never skipped", note)


if __name__ == "__main__":
    unittest.main()
