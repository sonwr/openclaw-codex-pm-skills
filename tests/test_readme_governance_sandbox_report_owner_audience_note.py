from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportOwnerAudienceNoteTests(unittest.TestCase):
    def test_readme_links_owner_audience_note(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_REPORT_OWNER_AUDIENCE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_REPORT_OWNER_AUDIENCE_NOTE.md').exists())

    def test_note_mentions_owner_and_audience(self):
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_REPORT_OWNER_AUDIENCE_NOTE.md').read_text(encoding='utf-8').lower()
        self.assertIn('owner', note)
        self.assertIn('audience', note)
        self.assertIn('bundle', note)


if __name__ == '__main__':
    unittest.main()
