from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioInputsAliasNoteTest(unittest.TestCase):
    def test_readme_mentions_scenario_inputs_alias_note(self) -> None:
        readme = Path("README.md").read_text()
        self.assertIn(
            "docs/GOVERNANCE_SANDBOX_SCENARIO_INPUTS_ALIAS_NOTE.md",
            readme,
        )


if __name__ == "__main__":
    unittest.main()
