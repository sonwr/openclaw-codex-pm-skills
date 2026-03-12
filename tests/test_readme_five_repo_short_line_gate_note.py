from pathlib import Path


def test_readme_mentions_five_repo_short_line_gate_note() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/OPENCLAW_PM_FIVE_REPO_SHORT_LINE_GATE_NOTE.md" in text
