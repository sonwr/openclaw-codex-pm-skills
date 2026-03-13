from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxPresetAliasFieldNoteTests(unittest.TestCase):
    def test_note_exists_with_repo5_scenario_file_cues(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_PRESET_ALIAS_FIELD_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("preset_alias", note)
        self.assertIn("JSON/YAML scenario", note)
        self.assertIn("canonical preset key", note)


if __name__ == "__main__":
    unittest.main()
