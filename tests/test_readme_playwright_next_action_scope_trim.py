from __future__ import annotations

from pathlib import Path
import unittest


class ReadmePlaywrightNextActionScopeTrimTests(unittest.TestCase):
    def test_readme_mentions_playwright_next_action_scope_trim_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_NEXT_ACTION_SCOPE_TRIM.md", readme)
        self.assertTrue((root / "docs" / "WEB_QA_PLAYWRIGHT_NEXT_ACTION_SCOPE_TRIM.md").exists())


if __name__ == "__main__":
    unittest.main()
