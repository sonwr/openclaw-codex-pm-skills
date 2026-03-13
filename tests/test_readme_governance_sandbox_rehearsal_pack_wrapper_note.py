from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxRehearsalPackWrapperNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_rehearsal_pack_wrapper_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_REHEARSAL_PACK_WRAPPER_NOTE.md", readme)

    def test_note_mentions_scenario_rehearsal_pack_and_report_bundle(self) -> None:
        note = (ROOT / "docs" / "GOVERNANCE_SANDBOX_REHEARSAL_PACK_WRAPPER_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("scenario_rehearsal_pack", note)
        self.assertIn("JSON/Markdown/HTML report bundle", note)


if __name__ == "__main__":
    unittest.main()
