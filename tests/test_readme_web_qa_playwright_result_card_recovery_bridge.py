from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaPlaywrightResultCardRecoveryBridgeTests(unittest.TestCase):
    def test_readme_mentions_result_card_recovery_bridge(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_RESULT_CARD_RECOVERY_BRIDGE.md", readme)
        self.assertTrue((ROOT / "docs" / "WEB_QA_PLAYWRIGHT_RESULT_CARD_RECOVERY_BRIDGE.md").exists())


if __name__ == "__main__":
    unittest.main()
