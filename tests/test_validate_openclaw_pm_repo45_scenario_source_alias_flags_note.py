import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')


class OpenClawPmRepo45ScenarioSourceAliasFlagsNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_source_alias_flags_note(self) -> None:
        self.assertIn('docs/OPENCLAW_PM_REPO45_SCENARIO_SOURCE_ALIAS_FLAGS_NOTE.md', README)
        self.assertTrue((ROOT / 'docs' / 'OPENCLAW_PM_REPO45_SCENARIO_SOURCE_ALIAS_FLAGS_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
