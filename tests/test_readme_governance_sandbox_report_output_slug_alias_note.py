from pathlib import Path
import unittest


class ReadmeGovernanceSandboxReportOutputSlugAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_report_output_slug_alias_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_SLUG_ALIAS_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'GOVERNANCE_SANDBOX_REPORT_OUTPUT_SLUG_ALIAS_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
