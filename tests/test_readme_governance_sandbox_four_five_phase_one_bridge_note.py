from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxFourFivePhaseOneBridgeNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_four_five_phase_one_bridge_note(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/GOVERNANCE_SANDBOX_FOUR_FIVE_PHASE_ONE_BRIDGE_NOTE.md', readme)
        self.assertTrue((ROOT / 'docs' / 'GOVERNANCE_SANDBOX_FOUR_FIVE_PHASE_ONE_BRIDGE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
