from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoResultCardAuditTests(unittest.TestCase):
    def test_readme_mentions_web_demo_result_card_audit(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_AUDIT.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_AUDIT.md").exists())


if __name__ == "__main__":
    unittest.main()
