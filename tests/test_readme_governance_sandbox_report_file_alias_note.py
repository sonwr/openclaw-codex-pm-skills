from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportFileAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_report_file_alias_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_REPORT_FILE_ALIAS_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_REPORT_FILE_ALIAS_NOTE.md', readme)
        self.assertIn('report-file alias', note)
        self.assertIn('repo 5', note)


if __name__ == '__main__':
    unittest.main()
