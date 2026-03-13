from pathlib import Path


def test_readme_mentions_openclaw_pm_five_repo_active_check_note() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/OPENCLAW_PM_FIVE_REPO_ACTIVE_CHECK_NOTE.md" in text
    assert Path("docs/OPENCLAW_PM_FIVE_REPO_ACTIVE_CHECK_NOTE.md").exists()
