from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'OPENCLAW_PM_REPO45_REPORT_OUTPUT_TAG_ALIAS_NOTE.md'


class ReadmeRepo45ReportOutputTagAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_report_output_tag_alias_note(self) -> None:
        readme = README.read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_TAG_ALIAS_NOTE.md', readme)

    def test_repo45_report_output_tag_alias_note_mentions_phase_one_bundle_alias(self) -> None:
        note = NOTE.read_text(encoding='utf-8')
        self.assertIn('report_output_tag', note)
        self.assertIn('JSON/Markdown/HTML bundle', note)
        self.assertIn('validator', note)


if __name__ == '__main__':
    unittest.main()
