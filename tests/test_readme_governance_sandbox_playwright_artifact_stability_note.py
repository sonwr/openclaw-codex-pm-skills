from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeGovernanceSandboxPlaywrightArtifactStabilityNoteTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_playwright_artifact_stability_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_PLAYWRIGHT_ARTIFACT_STABILITY_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'GOVERNANCE_SANDBOX_PLAYWRIGHT_ARTIFACT_STABILITY_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
