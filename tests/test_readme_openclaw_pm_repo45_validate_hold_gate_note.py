from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_openclaw_pm_repo45_validate_hold_gate_note() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/OPENCLAW_PM_REPO45_VALIDATE_HOLD_GATE_NOTE.md" in readme
    assert (ROOT / "docs" / "OPENCLAW_PM_REPO45_VALIDATE_HOLD_GATE_NOTE.md").exists()
