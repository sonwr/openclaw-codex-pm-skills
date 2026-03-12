from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_FILE_FIRST_RULE.md"


class ReadmeGovernanceSandboxScenarioFileFirstRuleTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_file_first_rule(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_FIRST_RULE.md", readme)

    def test_note_mentions_reproducible_artifact(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("one scenario file first", note)
        self.assertIn("reproducible scenario artifact", note)


if __name__ == "__main__":
    unittest.main()
