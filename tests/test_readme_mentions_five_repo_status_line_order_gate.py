from pathlib import Path


def test_readme_mentions_five_repo_status_line_order_gate() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/OPENCLAW_PM_FIVE_REPO_STATUS_LINE_ORDER_GATE.md" in text
