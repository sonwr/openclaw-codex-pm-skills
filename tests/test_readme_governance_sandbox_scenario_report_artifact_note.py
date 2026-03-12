import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md"


class ReadmeGovernanceSandboxScenarioReportArtifactNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_artifact_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md", readme)
        self.assertIn("named markdown/html/json memo bundle", readme)

    def test_governance_sandbox_scenario_report_artifact_note_keeps_bundle_visible(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("one scenario file", note)
        self.assertIn("JSON, Markdown, and HTML outputs", note)
        self.assertIn("artifact paths are visible", note)


if __name__ == "__main__":
    unittest.main()
