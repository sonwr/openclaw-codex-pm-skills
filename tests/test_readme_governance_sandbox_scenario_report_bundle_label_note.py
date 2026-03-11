from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_LABEL_NOTE.md"


def test_readme_mentions_scenario_report_bundle_label_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_BUNDLE_LABEL_NOTE.md" in readme
    assert "report bundle label" in readme


def test_scenario_report_bundle_label_note_keeps_bundle_naming_stable() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "stable report bundle label" in note
    assert "JSON, Markdown, and HTML artifacts" in note
