from pathlib import Path
import unittest


class ReadmeGovernanceSandboxTraitPresetPhaseOneNoteTest(unittest.TestCase):
    def test_readme_mentions_trait_preset_phase_one_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_TRAIT_PRESET_PHASE_ONE_NOTE.md", readme)
        self.assertTrue((root / "docs" / "GOVERNANCE_SANDBOX_TRAIT_PRESET_PHASE_ONE_NOTE.md").exists())


if __name__ == "__main__":
    unittest.main()
