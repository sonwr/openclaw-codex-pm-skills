from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxLinkTests(unittest.TestCase):
    def test_readme_keeps_web_demo_form_proof_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_FORM_PROOF.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_FORM_PROOF.md", readme)

    def test_readme_keeps_scenario_report_alias_expansion_link(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        doc = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION.md"

        self.assertTrue(doc.exists())
        self.assertIn("docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION.md", readme)


if __name__ == "__main__":
    unittest.main()
