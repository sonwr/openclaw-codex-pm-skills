from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxHtmlHeadingEscapeCheckTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_html_heading_escape_check(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_HTML_HEADING_ESCAPE_CHECK.md", readme)
        self.assertTrue((ROOT / "docs" / "WEB_QA_PLAYWRIGHT_HTML_HEADING_ESCAPE_CHECK.md").exists())


if __name__ == "__main__":
    unittest.main()
