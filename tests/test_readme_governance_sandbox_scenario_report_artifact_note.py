from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md"


def test_readme_mentions_governance_sandbox_scenario_report_artifact_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_ARTIFACT_NOTE.md" in readme
    assert NOTE.exists()


def test_governance_sandbox_scenario_report_artifact_note_keeps_bundle_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one scenario file" in note
    assert "one generated markdown artifact" in note
    assert "one generated html artifact" in note
