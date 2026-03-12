from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxWebDemoUiUxPlaywrightBridgeTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_ui_ux_playwright_bridge(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md', readme)
        self.assertTrue((root / 'docs' / 'GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md').exists())


if __name__ == '__main__':
    unittest.main()
