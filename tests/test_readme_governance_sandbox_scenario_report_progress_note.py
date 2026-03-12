from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioReportProgressNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_progress_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROGRESS_NOTE.md', readme)

    def test_note_mentions_imported_scenario_and_validated_bundle(self) -> None:
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_PROGRESS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('imported scenario file', note)
        self.assertIn('validated report bundle', note)


if __name__ == '__main__':
    unittest.main()
