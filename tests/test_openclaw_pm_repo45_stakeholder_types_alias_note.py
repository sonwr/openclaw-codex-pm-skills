from pathlib import Path
import unittest


class ReadmeRepo45StakeholderTypesAliasNoteTest(unittest.TestCase):
    def test_repo45_stakeholder_types_alias_note_exists(self) -> None:
        text = (Path(__file__).resolve().parents[1] / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_STAKEHOLDER_TYPES_ALIAS_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
