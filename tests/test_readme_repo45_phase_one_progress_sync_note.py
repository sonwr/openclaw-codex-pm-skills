from __future__ import annotations

from pathlib import Path
import unittest


class ReadmeRepo45PhaseOneProgressSyncNoteTests(unittest.TestCase):
    def test_readme_mentions_repo45_phase_one_progress_sync_note(self) -> None:
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')

        self.assertIn('docs/OPENCLAW_PM_REPO45_PHASE_ONE_PROGRESS_SYNC_NOTE.md', readme)
        self.assertTrue((root / 'docs' / 'OPENCLAW_PM_REPO45_PHASE_ONE_PROGRESS_SYNC_NOTE.md').exists())


if __name__ == '__main__':
    unittest.main()
