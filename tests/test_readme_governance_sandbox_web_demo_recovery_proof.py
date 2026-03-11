from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoRecoveryProofTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_recovery_proof(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_RECOVERY_PROOF.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_RECOVERY_PROOF.md").exists())


if __name__ == "__main__":
    unittest.main()
