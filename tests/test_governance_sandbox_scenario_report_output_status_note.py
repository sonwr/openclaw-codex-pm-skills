from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GovernanceSandboxScenarioReportOutputStatusNoteTest(unittest.TestCase):
    def test_note_mentions_scenario_input_and_report_outputs(self) -> None:
        text = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_OUTPUT_STATUS_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('scenario-file input', text)
        self.assertIn('JSON / Markdown / HTML report outputs', text)
        self.assertIn('repo 4 plus repo 5 visible on every pass', text)

if __name__ == '__main__':
    unittest.main()
