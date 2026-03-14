from pathlib import Path


def test_validate_openclaw_pm_repo45_scenario_source_uri_alias_note() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    note = (root / "docs" / "OPENCLAW_PM_REPO45_SCENARIO_SOURCE_URI_ALIAS_NOTE.md").read_text(encoding="utf-8")

    assert "docs/OPENCLAW_PM_REPO45_SCENARIO_SOURCE_URI_ALIAS_NOTE.md" in readme
    assert "scenario_source_uri" in note
    assert "five-line report" in note
