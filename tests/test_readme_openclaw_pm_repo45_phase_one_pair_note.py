import unittest
from pathlib import Path


class ReadmeRepo45PhaseOnePairNoteTest(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_pair_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_PHASE_ONE_PAIR_NOTE.md', readme)


if __name__ == '__main__':
    unittest.main()
