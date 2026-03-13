from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoUiPlaywrightPhaseNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_PLAYWRIGHT_PHASE_NOTE.md', readme)

    def test_note_mentions_ui_ux_and_playwright(self) -> None:
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_WEB_DEMO_UI_PLAYWRIGHT_PHASE_NOTE.md').read_text(encoding='utf-8')
        self.assertIn('UI/UX', note)
        self.assertIn('Playwright-interactive', note)


if __name__ == '__main__':
    unittest.main()
