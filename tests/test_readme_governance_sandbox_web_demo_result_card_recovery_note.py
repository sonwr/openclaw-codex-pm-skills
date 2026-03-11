import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxWebDemoResultCardRecoveryNoteTest(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_web_demo_result_card_recovery_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_RECOVERY_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_RECOVERY_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
