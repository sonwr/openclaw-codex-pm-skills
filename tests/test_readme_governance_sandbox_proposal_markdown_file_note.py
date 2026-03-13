from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxProposalMarkdownFileNoteTests(unittest.TestCase):
    def test_readme_mentions_proposal_markdown_file_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_MARKDOWN_FILE_NOTE.md", readme)
        self.assertTrue(
            (ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_MARKDOWN_FILE_NOTE.md").exists()
        )

    def test_note_mentions_neighboring_markdown_file_and_report_bundle(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_MARKDOWN_FILE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("neighboring markdown file", doc)
        self.assertIn("report bundle", doc)


if __name__ == "__main__":
    unittest.main()
