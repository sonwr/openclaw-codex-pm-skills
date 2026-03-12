from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_SHEET_BUNDLE_NOTE.md"


class ReadmeGovernanceSandboxScenarioSheetBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_sheet_bundle_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_SHEET_BUNDLE_NOTE.md", readme)

    def test_note_mentions_reproducible_scenario_artifact(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("scenario input and report-ready output metadata together", note)
        self.assertIn("reproducible scenario artifact", note)


if __name__ == "__main__":
    unittest.main()
