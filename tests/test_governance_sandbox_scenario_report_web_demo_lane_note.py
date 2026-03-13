from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportWebDemoLaneNoteTest(unittest.TestCase):
    def test_note_keeps_delivery_order_visible(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_WEB_DEMO_LANE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("scenario-file input first", doc)
        self.assertIn("JSON/Markdown/HTML report bundle second", doc)
        self.assertIn("trait presets third", doc)
        self.assertIn("web demo work only after", doc)

    def test_note_mentions_ui_ux_and_playwright_stability_rules(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_WEB_DEMO_LANE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("one form, one primary action, and one result card", doc)
        self.assertIn("Playwright-interactive stability rules", doc)
        self.assertIn("failure recovery", doc)


if __name__ == "__main__":
    unittest.main()
