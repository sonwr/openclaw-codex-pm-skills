from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_HANDOFF_NOTE.md"


def test_readme_mentions_scenario_report_owner_handoff_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_OWNER_HANDOFF_NOTE.md" in readme
    assert "owner-facing sentence" in readme


def test_scenario_report_owner_handoff_note_keeps_bundle_and_owner_scope() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "JSON, Markdown, and HTML report bundle" in note
    assert "one next action" in note
