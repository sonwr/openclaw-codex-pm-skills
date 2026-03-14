from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45ReportOutputKeyAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_report_output_key_alias_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_KEY_ALIAS_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_REPO45_REPORT_OUTPUT_KEY_ALIAS_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
