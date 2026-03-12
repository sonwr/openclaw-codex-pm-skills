from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenClawPmSmallValidatedSliceNoteTests(unittest.TestCase):
    def test_readme_mentions_small_validated_slice_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_SMALL_VALIDATED_SLICE_NOTE.md', readme)

    def test_note_mentions_small_validated_improvement(self) -> None:
        doc = (ROOT / 'docs' / 'OPENCLAW_PM_SMALL_VALIDATED_SLICE_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('small validated improvement', doc)
        self.assertIn('test evidence', doc)


if __name__ == '__main__':
    unittest.main()
