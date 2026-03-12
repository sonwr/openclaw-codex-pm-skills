import unittest
from pathlib import Path


class ReadmeGovernanceSandboxScenarioFileReportBundleStartNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_file_report_bundle_start_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn(
            "docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_BUNDLE_START_NOTE.md",
            readme,
        )
        self.assertIn("one JSON or YAML scenario input tied to one validated markdown/html/json report bundle", readme)


if __name__ == "__main__":
    unittest.main()
