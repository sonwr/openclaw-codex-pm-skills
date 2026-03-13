from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FiveRepoRepo45PriorityGateTests(unittest.TestCase):
    def test_repo45_priority_gate_doc_mentions_non_skip_rule(self) -> None:
        doc = (ROOT / "docs" / "FIVE_REPO_REPO45_PRIORITY_GATE.md").read_text(encoding="utf-8")

        self.assertIn("repository 4 (`oss-launchpad-cli`)", doc)
        self.assertIn("repository 5 (`governance-sandbox`)", doc)
        self.assertIn("scenario file inputs", doc)
        self.assertIn("markdown/html report outputs", doc)


if __name__ == "__main__":
    unittest.main()
