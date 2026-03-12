from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportBundleReviewTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_bundle_review_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_REVIEW.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_REVIEW.md").exists())


if __name__ == "__main__":
    unittest.main()
