from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45ProgressPairSmallSliceNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_progress_pair_small_slice_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_PROGRESS_PAIR_SMALL_SLICE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_PROGRESS_PAIR_SMALL_SLICE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
