from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoDownloadScopeNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_download_scope_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_DOWNLOAD_SCOPE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_DOWNLOAD_SCOPE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
