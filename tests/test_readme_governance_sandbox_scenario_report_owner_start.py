from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioReportOwnerStartTests(unittest.TestCase):
    def test_readme_mentions_owner_start_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_START.md', readme)

    def test_owner_start_note_mentions_owner_and_report_bundle(self) -> None:
        doc = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_START.md').read_text(encoding='utf-8')
        self.assertIn('owner field', doc)
        self.assertIn('JSON/Markdown/HTML report bundle', doc)


if __name__ == '__main__':
    unittest.main()
