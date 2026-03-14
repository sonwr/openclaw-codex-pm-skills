import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ReadmeRepo45ScenarioReportAliasLaneTests(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_report_alias_lane(self) -> None:
        self.assertIn("docs/OPENCLAW_PM_REPO45_SCENARIO_REPORT_ALIAS_LANE.md", README)


if __name__ == "__main__":
    unittest.main()
