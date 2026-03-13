from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeOpenclawPmRepo45ProgressPairGateNoteTests(unittest.TestCase):
    def test_readme_mentions_openclaw_pm_repo45_progress_pair_gate_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_PROGRESS_PAIR_GATE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_PROGRESS_PAIR_GATE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
