import unittest
from pathlib import Path


class ReadmeFiveRepoValidateLoopNoteTests(unittest.TestCase):
    def test_readme_mentions_five_repo_validate_loop_note(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("docs/OPENCLAW_PM_FIVE_REPO_VALIDATE_LOOP_NOTE.md", readme)


if __name__ == "__main__":
    unittest.main()
