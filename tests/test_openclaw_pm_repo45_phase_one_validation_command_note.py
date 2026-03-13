from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenClawPmRepo45PhaseOneValidationCommandNoteTest(unittest.TestCase):
    def test_note_mentions_repo45_phase_one_validation_gate(self) -> None:
        text = (ROOT / "docs" / "OPENCLAW_PM_REPO45_PHASE_ONE_VALIDATION_COMMAND_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario-file input plus generated report artifacts", text)
        self.assertIn("repo 4 plus repo 5 visible on every pass", text)
        self.assertIn("validation before commit/push", text)


if __name__ == "__main__":
    unittest.main()
