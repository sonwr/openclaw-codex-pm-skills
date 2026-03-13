from __future__ import annotations

import unittest
from pathlib import Path


class ReadmeRepo45ValidateThenPushStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_validate_then_push_status_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/OPENCLAW_PM_REPO45_VALIDATE_THEN_PUSH_STATUS_NOTE.md", readme)
        self.assertTrue((root / "docs" / "OPENCLAW_PM_REPO45_VALIDATE_THEN_PUSH_STATUS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
