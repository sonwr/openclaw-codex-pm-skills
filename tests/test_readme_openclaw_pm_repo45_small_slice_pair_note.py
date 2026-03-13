from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeOpenclawPmRepo45SmallSlicePairNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_SMALL_SLICE_PAIR_NOTE.md", readme)

    def test_note_mentions_repo4_repo5_and_validation(self) -> None:
        note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_SMALL_SLICE_PAIR_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("repo 4", note)
        self.assertIn("repo 5", note)
        self.assertIn("validator-backed", note)
        self.assertIn("scenario-file/report slice", note)


if __name__ == "__main__":
    unittest.main()
