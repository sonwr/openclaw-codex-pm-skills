import unittest
from pathlib import Path


class ReadmeGovernanceSandboxScenarioReportSynopsisAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_report_synopsis_alias_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_SYNOPSIS_ALIAS_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
