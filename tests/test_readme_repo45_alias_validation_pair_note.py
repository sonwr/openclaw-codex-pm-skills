from pathlib import Path


def test_readme_mentions_repo45_alias_validation_pair_note() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/OPENCLAW_PM_REPO45_ALIAS_VALIDATION_PAIR_NOTE.md" in text
