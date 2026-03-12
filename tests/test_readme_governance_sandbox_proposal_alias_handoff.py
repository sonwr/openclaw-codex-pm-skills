from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxProposalAliasHandoffTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_proposal_alias_handoff(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_ALIAS_HANDOFF.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_ALIAS_HANDOFF.md").exists())


if __name__ == "__main__":
    unittest.main()
