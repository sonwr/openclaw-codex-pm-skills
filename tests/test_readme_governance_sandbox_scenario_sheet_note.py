from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioSheetNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_sheet_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_SHEET_NOTE.md", readme)
        self.assertTrue(Path("docs/GOVERNANCE_SANDBOX_SCENARIO_SHEET_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
