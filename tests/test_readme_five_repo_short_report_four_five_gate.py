from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FiveRepoShortReportFourFiveGateTests(unittest.TestCase):
    def test_readme_mentions_short_report_four_five_gate_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_FIVE_REPO_SHORT_REPORT_FOUR_FIVE_GATE.md", readme)

    def test_note_mentions_repo_four_and_repo_five_presence(self) -> None:
        note = (ROOT / "docs" / "OPENCLAW_PM_FIVE_REPO_SHORT_REPORT_FOUR_FIVE_GATE.md").read_text(encoding="utf-8")
        self.assertIn("Repo 4 and repo 5 must appear", note)
        self.assertIn("exactly five short lines", note)

if __name__ == "__main__":
    unittest.main()
