from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportReadersAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_report_readers_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_READERS_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_READERS_ALIAS_NOTE.md").exists())
