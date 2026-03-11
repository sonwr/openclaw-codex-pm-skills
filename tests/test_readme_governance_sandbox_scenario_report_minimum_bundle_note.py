import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioReportMinimumBundleNoteTest(unittest.TestCase):
    def test_readme_mentions_scenario_report_minimum_bundle_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_MINIMUM_BUNDLE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_MINIMUM_BUNDLE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
