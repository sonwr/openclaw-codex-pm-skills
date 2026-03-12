from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaReplayHandoffCardTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/WEB_QA_REPLAY_HANDOFF_CARD.md', readme)
        self.assertTrue((ROOT / 'docs' / 'WEB_QA_REPLAY_HANDOFF_CARD.md').exists())


if __name__ == '__main__':
    unittest.main()
