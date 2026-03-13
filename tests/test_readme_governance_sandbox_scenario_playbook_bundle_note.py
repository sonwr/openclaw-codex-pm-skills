import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_PLAYBOOK_BUNDLE_NOTE.md"


class ReadmeGovernanceSandboxScenarioPlaybookBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_playbook_bundle_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_PLAYBOOK_BUNDLE_NOTE.md", readme)
        self.assertTrue(NOTE.exists())


if __name__ == "__main__":
    unittest.main()
