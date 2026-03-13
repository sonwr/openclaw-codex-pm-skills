from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_openclaw_pm_repo45_phase_one_delivery_order_note() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/OPENCLAW_PM_REPO45_PHASE_ONE_DELIVERY_ORDER_NOTE.md" in readme
    note = (ROOT / "docs" / "OPENCLAW_PM_REPO45_PHASE_ONE_DELIVERY_ORDER_NOTE.md").read_text(encoding="utf-8")
    assert "scenario-file input support first" in note
    assert "JSON/Markdown/HTML report bundle second" in note
