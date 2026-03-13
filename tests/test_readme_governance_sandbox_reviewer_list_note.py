from pathlib import Path
import unittest

README = Path(__file__).resolve().parents[1] / 'README.md'


class ReadmeGovernanceSandboxReviewerListNoteTests(unittest.TestCase):
    def test_readme_mentions_reviewer_list_note(self) -> None:
        text = README.read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_REVIEWER_LIST_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
