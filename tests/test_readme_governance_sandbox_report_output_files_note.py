from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_NOTE.md"


class GovernanceSandboxReportOutputFilesNoteTests(unittest.TestCase):
    def test_readme_mentions_report_output_files_note(self) -> None:
        readme = README.read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_NOTE.md", readme)
        self.assertTrue(NOTE.exists())

    def test_note_keeps_nested_files_mapping_visible(self) -> None:
        note = NOTE.read_text(encoding="utf-8")

        self.assertIn("report.outputs.files", note)
        self.assertIn("files.json", note)
        self.assertIn("files.markdown", note)
        self.assertIn("files.html", note)


if __name__ == "__main__":
    unittest.main()
