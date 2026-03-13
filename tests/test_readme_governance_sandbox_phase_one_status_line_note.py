from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxPhaseOneStatusLineNoteTests(unittest.TestCase):
    def test_readme_mentions_phase_one_status_line_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PHASE_ONE_STATUS_LINE_NOTE.md", readme)

    def test_note_mentions_scenario_file_and_markdown_html_report(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PHASE_ONE_STATUS_LINE_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario-file input support", doc)
        self.assertIn("markdown/html report generation", doc)


if __name__ == "__main__":
    unittest.main()
