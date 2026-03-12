from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioInputWrapperNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_input_wrapper_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn(
            "docs/GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md",
            readme,
        )
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
