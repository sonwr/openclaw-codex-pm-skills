from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportSubtitleNoteTests(unittest.TestCase):
    def test_readme_mentions_report_subtitle_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_SUBTITLE_NOTE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_SUBTITLE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
