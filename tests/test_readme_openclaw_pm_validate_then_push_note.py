import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')


class ReadmeOpenClawPmValidateThenPushNoteTests(unittest.TestCase):
    def test_readme_mentions_openclaw_pm_validate_then_push_note(self) -> None:
        self.assertIn('docs/OPENCLAW_PM_VALIDATE_THEN_PUSH_NOTE.md', README)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_VALIDATE_THEN_PUSH_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
