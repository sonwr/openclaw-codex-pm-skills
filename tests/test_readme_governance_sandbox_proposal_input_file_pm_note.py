from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxProposalInputFilePmNoteTests(unittest.TestCase):
    def test_readme_mentions_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_PROPOSAL_INPUT_FILE_PM_NOTE.md", readme)

    def test_note_mentions_proposal_input_file_and_report_bundle(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PROPOSAL_INPUT_FILE_PM_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("proposal_input_file", note)
        self.assertIn("JSON/Markdown/HTML report bundle", note)


if __name__ == "__main__":
    unittest.main()
