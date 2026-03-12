from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmePmValidateThenPushActiveReposNoteTests(unittest.TestCase):
    def test_readme_mentions_pm_validate_then_push_active_repos_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/PM_VALIDATE_THEN_PUSH_ACTIVE_REPOS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "PM_VALIDATE_THEN_PUSH_ACTIVE_REPOS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
