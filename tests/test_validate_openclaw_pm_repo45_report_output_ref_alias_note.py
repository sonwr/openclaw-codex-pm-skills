from pathlib import Path
import unittest


class ValidateOpenclawPmRepo45ReportOutputRefAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_report_output_ref_alias_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        note = Path('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_REF_ALIAS_NOTE.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_REF_ALIAS_NOTE.md', readme)
        self.assertIn('report_output_ref', note)
        self.assertIn('JSON/Markdown/HTML report-bundle proof lane', note)


if __name__ == '__main__':
    unittest.main()
