from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioJson5ReportNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_json5_report_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_JSON5_REPORT_NOTE.md', readme)

    def test_note_mentions_json5_and_report_bundle(self) -> None:
        note = (ROOT / 'docs/GOVERNANCE_SANDBOX_SCENARIO_JSON5_REPORT_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('.json5', note)
        self.assertIn('markdown/html/json', note)


if __name__ == '__main__':
    unittest.main()
