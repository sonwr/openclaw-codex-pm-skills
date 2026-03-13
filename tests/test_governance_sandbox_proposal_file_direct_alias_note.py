from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxProposalFileDirectAliasNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_FILE_DIRECT_ALIAS_NOTE.md", readme)

    def test_note_mentions_direct_aliases(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_FILE_DIRECT_ALIAS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("proposal_file", doc)
        self.assertIn("proposal_path", doc)


if __name__ == "__main__":
    unittest.main()
