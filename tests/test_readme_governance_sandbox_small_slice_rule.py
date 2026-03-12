from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxSmallSliceRuleTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_small_slice_rule(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_SMALL_SLICE_RULE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SMALL_SLICE_RULE.md').exists())


if __name__ == '__main__':
    unittest.main()
