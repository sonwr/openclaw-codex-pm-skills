from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"


class ReadmeWebQaReportBundleOwnerHandoffTests(unittest.TestCase):
    def test_readme_mentions_web_qa_report_bundle_owner_handoff(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")

        self.assertIn("examples/web_qa_playwright_report_bundle_owner_handoff.md", readme)
        self.assertTrue((ROOT / "examples" / "web_qa_playwright_report_bundle_owner_handoff.md").exists())


if __name__ == "__main__":
    unittest.main()
