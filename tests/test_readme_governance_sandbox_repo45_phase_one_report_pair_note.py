from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxRepo45PhaseOneReportPairNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_report_pair_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPO45_PHASE_ONE_REPORT_PAIR_NOTE.md", readme)

    def test_note_mentions_repo4_repo5_and_phase_one_targets(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_REPO45_PHASE_ONE_REPORT_PAIR_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("oss-launchpad-cli", doc)
        self.assertIn("governance-sandbox", doc)
        self.assertIn("scenario-file input support", doc)
        self.assertIn("markdown/html report generation", doc)


if __name__ == "__main__":
    unittest.main()
