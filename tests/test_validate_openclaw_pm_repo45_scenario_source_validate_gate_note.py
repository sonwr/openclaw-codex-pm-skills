from __future__ import annotations

from pathlib import Path
import unittest


class ValidateOpenClawPmRepo45ScenarioSourceValidateGateNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_scenario_source_validate_gate_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_SCENARIO_SOURCE_VALIDATE_GATE_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'OPENCLAW_PM_REPO45_SCENARIO_SOURCE_VALIDATE_GATE_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
