import unittest
from pathlib import Path


class ReadmeRepo45ReportOutputSlugAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_report_output_slug_alias_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_SLUG_ALIAS_NOTE.md', readme)


if __name__ == '__main__':
    unittest.main()
