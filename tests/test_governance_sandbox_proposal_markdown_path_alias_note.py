import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
NOTE = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_MARKDOWN_PATH_ALIAS_NOTE.md").read_text(encoding="utf-8")


class GovernanceSandboxProposalMarkdownPathAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_MARKDOWN_PATH_ALIAS_NOTE.md", README)
        self.assertIn("proposal_markdown_path", NOTE)
        self.assertIn("repo 4 + repo 5 status visible", NOTE)


if __name__ == "__main__":
    unittest.main()
