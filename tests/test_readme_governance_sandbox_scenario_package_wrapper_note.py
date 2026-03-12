from pathlib import Path
import unittest


class ReadmeGovernanceSandboxScenarioPackageWrapperNoteTests(unittest.TestCase):
    def test_readme_mentions_scenario_package_wrapper_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/GOVERNANCE_SANDBOX_SCENARIO_PACKAGE_WRAPPER_NOTE.md', readme)
        note = root / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_PACKAGE_WRAPPER_NOTE.md'
        self.assertTrue(note.exists())
        self.assertIn('scenario_package', note.read_text(encoding='utf-8'))
        self.assertIn('JSON/Markdown/HTML report stack', note.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
