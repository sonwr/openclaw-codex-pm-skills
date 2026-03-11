from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaPlaywrightSignoffReportScopeBriefTests(unittest.TestCase):
    def test_readme_mentions_web_qa_playwright_signoff_report_scope_brief(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_SIGNOFF_REPORT_SCOPE_BRIEF.md", readme)
        self.assertTrue((ROOT / "docs" / "WEB_QA_PLAYWRIGHT_SIGNOFF_REPORT_SCOPE_BRIEF.md").exists())


if __name__ == "__main__":
    unittest.main()
