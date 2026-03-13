from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_FIXTURE_PROOF_NOTE.md"


class ReadmeGovernanceSandboxScenarioReportFixtureProofNoteTests(unittest.TestCase):
    def test_readme_mentions_fixture_proof_note(self) -> None:
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_FIXTURE_PROOF_NOTE.md", README.read_text(encoding="utf-8"))

    def test_note_mentions_fixture_path_and_report_trio(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("scenario fixture path", note)
        self.assertIn("JSON / Markdown / HTML artifact trio", note)


if __name__ == "__main__":
    unittest.main()
