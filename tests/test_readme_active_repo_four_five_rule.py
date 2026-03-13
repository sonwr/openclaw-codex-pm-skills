from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeActiveRepoFourFiveRuleTests(unittest.TestCase):
    def test_readme_mentions_active_repo_four_five_rule(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_ACTIVE_REPO_FOUR_FIVE_RULE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_ACTIVE_REPO_FOUR_FIVE_RULE.md').exists())


if __name__ == '__main__':
    unittest.main()
