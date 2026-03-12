from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GovernanceSandboxTraitPresetBundleQueueNoteTests(unittest.TestCase):
    def test_readme_mentions_trait_preset_bundle_queue_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_TRAIT_PRESET_BUNDLE_QUEUE_NOTE.md", readme)

    def test_note_mentions_first_trait_preset_bundle(self) -> None:
        doc = (ROOT / "docs" / "GOVERNANCE_SANDBOX_TRAIT_PRESET_BUNDLE_QUEUE_NOTE.md").read_text(encoding="utf-8")
        self.assertIn("dao", doc)
        self.assertIn("community", doc)


if __name__ == "__main__":
    unittest.main()
