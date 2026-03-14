from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestValidateOpenclawPmRepo45UiPlaywrightPhaseNote(unittest.TestCase):
    def test_readme_mentions_openclaw_pm_repo45_ui_playwright_phase_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_UI_PLAYWRIGHT_PHASE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_UI_PLAYWRIGHT_PHASE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
