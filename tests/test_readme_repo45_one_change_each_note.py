from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeRepo45OneChangeEachNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_one_change_each_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_ONE_CHANGE_EACH_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'OPENCLAW_PM_REPO45_ONE_CHANGE_EACH_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
