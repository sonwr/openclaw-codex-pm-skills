from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioStudioNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_scenario_studio_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_STUDIO_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_STUDIO_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
