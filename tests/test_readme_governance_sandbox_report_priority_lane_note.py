from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxReportPriorityLaneNoteTests(unittest.TestCase):
    def test_readme_mentions_report_priority_lane_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_REPORT_PRIORITY_LANE_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
