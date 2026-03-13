from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeFiveRepoRepo45AlwaysActiveNoteTests(unittest.TestCase):
    def test_readme_mentions_five_repo_repo45_always_active_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_FIVE_REPO_REPO45_ALWAYS_ACTIVE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_FIVE_REPO_REPO45_ALWAYS_ACTIVE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
