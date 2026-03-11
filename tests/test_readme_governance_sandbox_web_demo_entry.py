from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxWebDemoEntryTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_entry_docs(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        required_docs = [
            "docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_REVIEW.md",
            "docs/GOVERNANCE_SANDBOX_WEB_DEMO_CHECKPOINT_RULE.md",
            "docs/GOVERNANCE_SANDBOX_WEB_DEMO_PROOF_LOOP.md",
            "docs/GOVERNANCE_SANDBOX_WEB_DEMO_ENTRY_CHECK.md",
        ]

        for doc in required_docs:
            with self.subTest(doc=doc):
                self.assertIn(doc, readme)
                self.assertTrue((root / doc).exists(), f"missing doc: {doc}")


if __name__ == "__main__":
    unittest.main()
