from pathlib import Path
import unittest


class OpenClawPmRepo45ReportOutputKeyAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_report_output_key_alias_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('report_output_key', readme)
        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_KEY_ALIAS_NOTE.md', readme)

    def test_note_mentions_report_output_key_alias(self) -> None:
        note = Path('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_KEY_ALIAS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('report_output_key', note)
        self.assertIn('JSON/Markdown/HTML report bundle', note)


if __name__ == '__main__':
    unittest.main()
