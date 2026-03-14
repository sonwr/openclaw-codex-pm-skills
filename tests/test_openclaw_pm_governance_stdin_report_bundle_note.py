from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenclawPmGovernanceStdinReportBundleNoteTests(unittest.TestCase):
    def test_note_exists_with_stdin_report_bundle_cues(self) -> None:
        note = (ROOT / "docs" / "OPENCLAW_PM_GOVERNANCE_STDIN_REPORT_BUNDLE_NOTE.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("stdin-fed JSON or YAML scenario replay", note)
        self.assertIn("markdown/html/json report bundle", note)
        self.assertIn("validation rerun", note)
        self.assertIn("docs/OPENCLAW_PM_GOVERNANCE_STDIN_REPORT_BUNDLE_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
