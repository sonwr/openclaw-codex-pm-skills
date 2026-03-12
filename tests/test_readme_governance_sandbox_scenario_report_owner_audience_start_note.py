from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioReportOwnerAudienceStartNoteTests(unittest.TestCase):
    def test_readme_keeps_owner_audience_start_note_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_START_NOTE.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_AUDIENCE_START_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
