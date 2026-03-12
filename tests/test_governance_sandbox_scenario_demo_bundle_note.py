import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")

class ReadmeGovernanceSandboxScenarioDemoBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_demo_bundle_note(self) -> None:
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_DEMO_BUNDLE_NOTE.md", README)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_DEMO_BUNDLE_NOTE.md").exists())

if __name__ == "__main__":
    unittest.main()
