from pathlib import Path
import unittest


class ReadmeGovernanceSandboxPriorityPairValidateThenPushNoteTest(unittest.TestCase):
    def test_readme_mentions_priority_pair_validate_then_push_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_VALIDATE_THEN_PUSH_NOTE.md", readme)
        self.assertTrue(Path("docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_VALIDATE_THEN_PUSH_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
