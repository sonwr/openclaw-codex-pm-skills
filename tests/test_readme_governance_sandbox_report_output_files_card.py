from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxReportOutputFilesCardTests(unittest.TestCase):
    def test_readme_mentions_report_output_files_card(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_CARD.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_OUTPUT_FILES_CARD.md").exists())


if __name__ == "__main__":
    unittest.main()
