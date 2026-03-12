from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxTopLevelProposalCopyMarkdownNoteTests(unittest.TestCase):
    def test_readme_mentions_top_level_proposal_copy_markdown_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_TOP_LEVEL_PROPOSAL_COPY_MARKDOWN_NOTE.md", readme)
        self.assertTrue(
            (ROOT / "docs" / "GOVERNANCE_SANDBOX_TOP_LEVEL_PROPOSAL_COPY_MARKDOWN_NOTE.md").exists()
        )


if __name__ == "__main__":
    unittest.main()
