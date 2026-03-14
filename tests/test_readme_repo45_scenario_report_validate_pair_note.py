from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestReadmeRepo45ScenarioReportValidatePairNote(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_report_validate_pair_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_SCENARIO_REPORT_VALIDATE_PAIR_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("docs/OPENCLAW_PM_REPO45_SCENARIO_REPORT_VALIDATE_PAIR_NOTE.md", readme)
        self.assertIn("five-line report", note)
        self.assertIn("validation", note)


if __name__ == "__main__":
    unittest.main()
