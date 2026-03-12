import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxProposalObjectNoteTest(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_proposal_object_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_OBJECT_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_OBJECT_NOTE.md").exists())
