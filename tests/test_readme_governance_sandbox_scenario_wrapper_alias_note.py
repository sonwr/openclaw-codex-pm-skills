from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioWrapperAliasNoteTest(unittest.TestCase):
    def test_readme_links_scenario_wrapper_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        rel = "docs/GOVERNANCE_SANDBOX_SCENARIO_WRAPPER_ALIAS_NOTE.md"
        self.assertIn(rel, readme)
        note = (ROOT / rel).read_text(encoding="utf-8")
        self.assertIn("scenario_payload", note)
        self.assertIn("proposal + stakeholder + report-bundle proof path", note)


if __name__ == "__main__":
    unittest.main()
