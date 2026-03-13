from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioNotebookWrapperNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_notebook_wrapper_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_NOTEBOOK_WRAPPER_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
