from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestReadmeGovernanceSandboxScenarioReportVerificationLane(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_verification_lane(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_VERIFICATION_LANE.md", readme)
        self.assertTrue((ROOT / "docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_VERIFICATION_LANE.md").exists())


if __name__ == "__main__":
    unittest.main()
