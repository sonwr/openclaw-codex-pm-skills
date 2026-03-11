from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeWebQaPlaywrightReplayInputStabilityTests(unittest.TestCase):
    def test_readme_mentions_replay_input_stability_doc(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_REPLAY_INPUT_STABILITY.md", readme)
        self.assertTrue((root / "docs" / "WEB_QA_PLAYWRIGHT_REPLAY_INPUT_STABILITY.md").exists())


if __name__ == "__main__":
    unittest.main()
