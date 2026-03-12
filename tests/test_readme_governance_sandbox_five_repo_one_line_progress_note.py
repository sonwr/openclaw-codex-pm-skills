from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxFiveRepoOneLineProgressNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_five_repo_one_line_progress_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_FIVE_REPO_ONE_LINE_PROGRESS_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_FIVE_REPO_ONE_LINE_PROGRESS_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
