from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxScenarioReportPhaseOneCheckTests(unittest.TestCase):
    def test_readme_mentions_phase_one_check_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PHASE_ONE_CHECK.md", readme)


if __name__ == "__main__":
    unittest.main()
