from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoUiUxPlaywrightBridgeTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_ui_ux_playwright_bridge_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md").exists())


if __name__ == "__main__":
    unittest.main()
