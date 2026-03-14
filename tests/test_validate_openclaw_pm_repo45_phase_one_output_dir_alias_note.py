from pathlib import Path
import unittest


class OpenClawPmRepo45PhaseOneOutputDirAliasNoteTest(unittest.TestCase):
    def test_readme_mentions_output_dir_alias_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn(
            "docs/OPENCLAW_PM_REPO45_PHASE_ONE_OUTPUT_DIR_ALIAS_NOTE.md",
            readme,
        )

    def test_note_exists_and_mentions_report_output_dir(self) -> None:
        note = Path("docs/OPENCLAW_PM_REPO45_PHASE_ONE_OUTPUT_DIR_ALIAS_NOTE.md")
        self.assertTrue(note.exists())
        content = note.read_text(encoding="utf-8")
        self.assertIn("report_output_dir", content)
        self.assertIn("repo 4", content)
        self.assertIn("repo 5", content)


if __name__ == "__main__":
    unittest.main()
