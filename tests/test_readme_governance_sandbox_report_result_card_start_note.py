from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_REPORT_RESULT_CARD_START_NOTE.md"


def test_readme_mentions_governance_sandbox_report_result_card_start_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_REPORT_RESULT_CARD_START_NOTE.md" in readme
    assert "scenario input and reviewer-visible report output" in readme


def test_governance_sandbox_report_result_card_start_note_keeps_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "import one scenario file" in note
    assert "render one result card" in note
    assert "verify one report download action" in note
