from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidateOpenClawPmRepo45PhaseOneRecheckNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_recheck_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_PHASE_ONE_RECHECK_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_PHASE_ONE_RECHECK_NOTE.md").exists())

    def test_note_mentions_repo4_and_repo5_priority_pair(self) -> None:
        doc = (ROOT / "docs" / "OPENCLAW_PM_REPO45_PHASE_ONE_RECHECK_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("oss-launchpad-cli", doc)
        self.assertIn("governance-sandbox", doc)
        self.assertIn("scenario file input first", doc)


if __name__ == "__main__":
    unittest.main()
