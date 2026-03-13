from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GovernanceSandboxScenarioReportFileAliasNoteTest(unittest.TestCase):
    def test_note_mentions_named_json_markdown_html_report_files(self) -> None:
        text = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_FILE_ALIAS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('scenario-file input plus generated report artifacts', text)
        self.assertIn('named JSON, Markdown, and HTML report files', text)
        self.assertIn('repo 4 plus repo 5 visible on every pass', text)

if __name__ == '__main__':
    unittest.main()
