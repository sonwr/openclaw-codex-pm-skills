from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioReplayBundleNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_replay_bundle_note(self) -> None:
        readme = Path('README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_REPLAY_BUNDLE_NOTE.md', readme)
        self.assertIn('one imported fixture tied to one regenerated JSON/Markdown/HTML report bundle', readme)


if __name__ == '__main__':
    unittest.main()
