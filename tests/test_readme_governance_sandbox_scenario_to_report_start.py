from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_TO_REPORT_START.md"


def test_readme_mentions_governance_sandbox_scenario_to_report_start_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_SCENARIO_TO_REPORT_START.md" in readme
    assert "scenario file -> one JSON/Markdown/HTML report bundle" in readme


def test_governance_sandbox_scenario_to_report_start_note_keeps_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one scenario file" in note
    assert "JSON, Markdown, and HTML outputs" in note
    assert "artifact paths are visible" in note
