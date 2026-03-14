from pathlib import Path


def test_validate_openclaw_pm_repo45_scenario_report_phase_order_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "OPENCLAW_PM_REPO45_SCENARIO_REPORT_PHASE_ORDER_NOTE.md" in readme
