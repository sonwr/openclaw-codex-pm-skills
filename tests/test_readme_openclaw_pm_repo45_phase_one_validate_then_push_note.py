from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeOpenclawPmRepo45PhaseOneValidateThenPushNoteTest(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_validate_then_push_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'OPENCLAW_PM_REPO45_PHASE_ONE_VALIDATE_THEN_PUSH_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_PHASE_ONE_VALIDATE_THEN_PUSH_NOTE.md', readme)
        self.assertIn('repo 5 stays scenario-file/report-first', note)
        self.assertIn('fresh validation rerun', note)


if __name__ == '__main__':
    unittest.main()
