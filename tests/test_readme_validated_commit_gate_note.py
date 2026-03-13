from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReadmeValidatedCommitGateNoteTests(unittest.TestCase):
    def test_readme_mentions_validated_commit_gate_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/OPENCLAW_PM_VALIDATED_COMMIT_GATE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_VALIDATED_COMMIT_GATE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
