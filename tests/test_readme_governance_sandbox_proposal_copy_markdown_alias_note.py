from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxProposalCopyMarkdownAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_proposal_copy_markdown_alias_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_COPY_MARKDOWN_ALIAS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_COPY_MARKDOWN_ALIAS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
