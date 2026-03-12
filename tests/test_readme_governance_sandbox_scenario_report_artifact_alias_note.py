from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportArtifactAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_report_artifact_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_ALIAS_NOTE.md", readme)

    def test_note_mentions_artifacts_alias_and_report_bundle(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_ALIAS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("report.outputs.artifacts", doc)
        self.assertIn("JSON/Markdown/HTML report bundle", doc)


if __name__ == "__main__":
    unittest.main()
