from pathlib import Path
import unittest


class ReadmeGovernanceSandboxWebDemoUiUxPlaywrightBridgeTest(unittest.TestCase):
    def test_readme_mentions_ui_ux_playwright_bridge_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_BRIDGE.md', readme)


if __name__ == '__main__':
    unittest.main()
