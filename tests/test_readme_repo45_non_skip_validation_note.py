from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45NonSkipValidationNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_non_skip_validation_note(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_NON_SKIP_VALIDATION_NOTE.md", text)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_NON_SKIP_VALIDATION_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
