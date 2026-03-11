from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioStakeholderAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_stakeholder_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_STAKEHOLDER_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_STAKEHOLDER_ALIAS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
