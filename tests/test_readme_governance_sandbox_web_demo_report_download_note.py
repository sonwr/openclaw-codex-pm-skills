from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoReportDownloadNoteTests(unittest.TestCase):
    def test_readme_mentions_web_demo_report_download_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_REPORT_DOWNLOAD_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_REPORT_DOWNLOAD_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
