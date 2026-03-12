from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_BASENAME_NOTE.md"


class ReadmeGovernanceSandboxScenarioReportOwnerBasenameNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_BASENAME_NOTE.md", readme)

    def test_note_mentions_owner_and_basename(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("shared report basename", note)
        self.assertIn("visible report owner handoff", note)


if __name__ == "__main__":
    unittest.main()
