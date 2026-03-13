from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45PhaseOneReportBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_report_bundle_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_PHASE_ONE_REPORT_BUNDLE_NOTE.md").read_text(encoding="utf-8")

        self.assertIn("docs/OPENCLAW_PM_REPO45_PHASE_ONE_REPORT_BUNDLE_NOTE.md", readme)
        self.assertIn("repo 4", note)
        self.assertIn("repo 5", note)
        self.assertIn("scenario file", note)
        self.assertIn("JSON/Markdown/HTML report bundle", note)


if __name__ == "__main__":
    unittest.main()
