from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ACTIVE_SLICE_NOTE.md"


class ReadmeGovernanceSandboxActiveSliceNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_active_slice_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ACTIVE_SLICE_NOTE.md", readme)

    def test_note_mentions_scenario_file_and_report_bundle_focus(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("scenario-file input first", note)
        self.assertIn("markdown/html/json report output", note)


if __name__ == "__main__":
    unittest.main()
