import unittest
from pathlib import Path


class OpenClawPmRepo45ProposalInputMarkdownPathNoteTest(unittest.TestCase):
    def test_note_is_linked_and_mentions_alias(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        note = (root / 'docs' / 'OPENCLAW_PM_REPO45_PROPOSAL_INPUT_MARKDOWN_PATH_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_PROPOSAL_INPUT_MARKDOWN_PATH_NOTE.md', readme)
        self.assertIn('proposal_input_markdown_path', note)
        self.assertIn('five-line report', note)


if __name__ == '__main__':
    unittest.main()
