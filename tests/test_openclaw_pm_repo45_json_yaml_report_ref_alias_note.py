from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OpenClawPmRepo45JsonYamlReportRefAliasNoteTests(unittest.TestCase):
    def test_note_exists_with_phase_one_cues(self) -> None:
        note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_JSON_YAML_REPORT_REF_ALIAS_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("JSON/YAML scenario file", note)
        self.assertIn("report_bundle_ref", note)
        self.assertIn("repo 4 active", note)


if __name__ == "__main__":
    unittest.main()
