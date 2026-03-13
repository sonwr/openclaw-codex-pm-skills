from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestValidateOpenclawPmRepo45PlaywrightRecoveryMiniLoopNote(unittest.TestCase):
    def test_readme_mentions_openclaw_pm_repo45_playwright_recovery_mini_loop_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_REPO45_PLAYWRIGHT_RECOVERY_MINI_LOOP_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "OPENCLAW_PM_REPO45_PLAYWRIGHT_RECOVERY_MINI_LOOP_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
