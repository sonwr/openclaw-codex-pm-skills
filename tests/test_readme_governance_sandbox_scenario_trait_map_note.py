from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_TRAIT_MAP_NOTE.md"


class ReadmeGovernanceSandboxScenarioTraitMapNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_trait_map_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_TRAIT_MAP_NOTE.md", readme)

    def test_note_mentions_report_bundle_proof(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("stakeholder_trait_map", note)
        self.assertIn("JSON/Markdown/HTML report bundle", note)


if __name__ == "__main__":
    unittest.main()
