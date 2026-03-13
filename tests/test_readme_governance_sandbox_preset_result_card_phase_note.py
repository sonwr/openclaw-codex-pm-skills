from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxPresetResultCardPhaseNoteTests(unittest.TestCase):
    def test_readme_mentions_preset_result_card_phase_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_PRESET_RESULT_CARD_PHASE_NOTE.md", readme)
        self.assertIn("preset-driven result-card work", readme)


if __name__ == "__main__":
    unittest.main()
