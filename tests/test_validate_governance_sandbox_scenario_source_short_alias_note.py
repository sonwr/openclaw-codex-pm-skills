from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioSourceShortAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_source_short_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_SOURCE_SHORT_ALIAS_NOTE.md", readme)

    def test_note_mentions_short_aliases_and_report_bundle(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_SOURCE_SHORT_ALIAS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario_src", doc)
        self.assertIn("source_href", doc)
        self.assertIn("report bundle", doc)


if __name__ == "__main__":
    unittest.main()
