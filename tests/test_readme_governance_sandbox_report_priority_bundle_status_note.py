from pathlib import Path
import unittest


class ReadmeGovernanceSandboxReportPriorityBundleStatusNoteTest(unittest.TestCase):
    def test_note_exists_with_priority_bundle_language(self) -> None:
        note = Path("docs/GOVERNANCE_SANDBOX_REPORT_PRIORITY_BUNDLE_STATUS_NOTE.md")
        self.assertTrue(note.exists())
        text = note.read_text(encoding="utf-8")
        self.assertIn("scenario file", text.lower())
        self.assertIn("json/markdown/html", text.lower())


if __name__ == "__main__":
    unittest.main()
