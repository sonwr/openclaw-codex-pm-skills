from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaPlaywrightNextActionFailedRefsNoteTests(unittest.TestCase):
    def test_readme_mentions_next_action_failed_refs_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_FAILED_REFS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "WEB_QA_PLAYWRIGHT_NEXT_ACTION_FAILED_REFS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
