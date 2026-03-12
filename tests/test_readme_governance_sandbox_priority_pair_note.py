from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_PRIORITY_PAIR_NOTE.md"


class ReadmeGovernanceSandboxPriorityPairNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_priority_pair_note(self) -> None:
        readme = README.read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PRIORITY_PAIR_NOTE.md", readme)

    def test_note_mentions_priority_pair(self) -> None:
        note = NOTE.read_text(encoding="utf-8")
        self.assertIn("scenario-file input", note)
        self.assertIn("markdown/html report output", note)


if __name__ == "__main__":
    unittest.main()
