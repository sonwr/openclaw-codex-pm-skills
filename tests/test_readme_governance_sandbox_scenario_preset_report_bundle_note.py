from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_PRESET_REPORT_BUNDLE_NOTE.md"


def test_readme_mentions_governance_sandbox_scenario_preset_report_bundle_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_SCENARIO_PRESET_REPORT_BUNDLE_NOTE.md" in readme
    assert NOTE.exists()


def test_governance_sandbox_scenario_preset_report_bundle_note_keeps_priority_order() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one scenario file" in note
    assert "one shared markdown/html/json report bundle" in note
    assert "preset-backed stakeholder mix" in note
