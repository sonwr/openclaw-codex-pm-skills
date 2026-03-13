from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenClawPmGovernancePhaseOneAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_phase_one_alias_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_GOVERNANCE_PHASE_ONE_ALIAS_NOTE.md', readme)

    def test_note_mentions_phase_one_order(self) -> None:
        note = (ROOT / 'docs' / 'OPENCLAW_PM_GOVERNANCE_PHASE_ONE_ALIAS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('scenario file import first', note)
        self.assertIn('JSON/Markdown/HTML report bundle second', note)


if __name__ == '__main__':
    unittest.main()
