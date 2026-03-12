from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioReportPhaseOneLoopTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_report_phase_one_loop(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_LOOP.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_LOOP.md").exists())
