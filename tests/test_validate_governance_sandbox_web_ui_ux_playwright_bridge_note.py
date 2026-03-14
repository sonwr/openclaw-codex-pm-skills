from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidateGovernanceSandboxWebUiUxPlaywrightBridgeNoteTests(unittest.TestCase):
    def test_readme_mentions_bridge_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_WEB_UI_UX_PLAYWRIGHT_BRIDGE_NOTE.md', readme)

    def test_note_keeps_ui_ux_and_playwright_bridge_visible(self) -> None:
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_WEB_UI_UX_PLAYWRIGHT_BRIDGE_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('UI/UX-first structure', note)
        self.assertIn('Playwright proof limited to one stable replay path', note)
        self.assertIn('JSON/YAML scenario-file support and Markdown/HTML report artifacts', note)


if __name__ == '__main__':
    unittest.main()
