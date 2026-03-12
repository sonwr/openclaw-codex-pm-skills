import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ReadmeGovernanceSandboxPriorityPairStatusNoteTests(unittest.TestCase):
    def test_readme_mentions_priority_pair_status_note(self) -> None:
        self.assertIn("docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_STATUS_NOTE.md", README)


if __name__ == "__main__":
    unittest.main()
