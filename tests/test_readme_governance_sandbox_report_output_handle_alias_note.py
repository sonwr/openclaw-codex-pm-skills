from __future__ import annotations

import unittest
from pathlib import Path


class ReadmeGovernanceSandboxReportOutputHandleAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_report_output_handle_alias_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('OPENCLAW_PM_REPO45_REPORT_OUTPUT_HANDLE_ALIAS_NOTE.md', readme)

    def test_note_mentions_governance_sandbox_report_output_handle_alias(self) -> None:
        note = Path('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_HANDLE_ALIAS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('report_output_handle', note)
        self.assertIn('repo 4 and repo 5', note)


if __name__ == '__main__':
    unittest.main()
