from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"


class ReadmeScenarioPlanWrapperNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_plan_wrapper_note(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_PLAN_WRAPPER_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_PLAN_WRAPPER_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
