import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeOpenclawPmRepo45ProposalCopyFileNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_proposal_copy_file_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_PROPOSAL_COPY_FILE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_REPO45_PROPOSAL_COPY_FILE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
