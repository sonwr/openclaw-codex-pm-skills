from pathlib import Path


def test_readme_mentions_five_repo_status_hold_order_note() -> None:
    text = Path("README.md").read_text(encoding="utf-8")
    assert "docs/OPENCLAW_PM_FIVE_REPO_STATUS_HOLD_ORDER_NOTE.md" in text
