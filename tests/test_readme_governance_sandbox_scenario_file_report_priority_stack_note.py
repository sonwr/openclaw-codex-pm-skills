import unittest
from pathlib import Path


class ReadmeGovernanceSandboxScenarioFileReportPriorityStackNoteTests(unittest.TestCase):
    def test_readme_mentions_priority_stack_note(self) -> None:
        readme = Path(__file__).resolve().parents[1] / 'README.md'
        text = readme.read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_PRIORITY_STACK_NOTE.md', text)


if __name__ == '__main__':
    unittest.main()
