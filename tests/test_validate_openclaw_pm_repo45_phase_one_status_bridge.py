from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRepo45PhaseOneStatusBridgeTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_status_bridge(self) -> None:
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        note = (ROOT / 'docs' / 'GOVERNANCE_SANDBOX_REPO45_PHASE_ONE_STATUS_BRIDGE.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_REPO45_PHASE_ONE_STATUS_BRIDGE.md', readme)
        self.assertIn('repo 4', note)
        self.assertIn('repo 5', note)
        self.assertIn('scenario file input', note)
        self.assertIn('JSON/Markdown/HTML report output', note)


if __name__ == '__main__':
    unittest.main()
