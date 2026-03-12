from pathlib import Path
import unittest


class ReadmeFiveRepoShortReportRuleTest(unittest.TestCase):
    def test_readme_mentions_five_repo_short_report_rule(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/GOVERNANCE_SANDBOX_FIVE_REPO_SHORT_REPORT_RULE.md", readme)


if __name__ == "__main__":
    unittest.main()
