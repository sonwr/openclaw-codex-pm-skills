from pathlib import Path
import unittest


class ReadmeRepo45ScenarioFileReportPairGateNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_file_report_pair_gate_note(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        readme = (repo / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_SCENARIO_FILE_REPORT_PAIR_GATE_NOTE.md', readme)
        self.assertTrue((repo / 'docs' / 'OPENCLAW_PM_REPO45_SCENARIO_FILE_REPORT_PAIR_GATE_NOTE.md').exists())
