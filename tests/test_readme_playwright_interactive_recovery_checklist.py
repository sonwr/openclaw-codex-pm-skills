from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmePlaywrightInteractiveRecoveryChecklistTests(unittest.TestCase):
    def test_readme_mentions_playwright_interactive_recovery_checklist(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/PLAYWRIGHT_INTERACTIVE_RECOVERY_CHECKLIST.md', readme)
        self.assertTrue((ROOT / 'docs' / 'PLAYWRIGHT_INTERACTIVE_RECOVERY_CHECKLIST.md').exists())


if __name__ == '__main__':
    unittest.main()
