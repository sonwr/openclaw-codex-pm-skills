from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxWebDemoPlaywrightRecoveryNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_playwright_recovery_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_RECOVERY_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_RECOVERY_NOTE.md").exists())
