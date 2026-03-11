from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeWebQaPlaywrightFailureOwnerLaneTests(unittest.TestCase):
    def test_readme_mentions_failure_owner_lane(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/WEB_QA_PLAYWRIGHT_FAILURE_OWNER_LANE.md", readme)
        self.assertTrue((ROOT / "docs" / "WEB_QA_PLAYWRIGHT_FAILURE_OWNER_LANE.md").exists())


if __name__ == "__main__":
    unittest.main()
