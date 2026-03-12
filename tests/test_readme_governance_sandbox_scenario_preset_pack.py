from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxScenarioPresetPackTests(unittest.TestCase):
    def test_readme_links_governance_sandbox_scenario_preset_pack(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_PRESET_PACK.md"

        self.assertTrue(note.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_PRESET_PACK.md", readme)
        self.assertIn("trait presets", note.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
