from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_DOWNLOAD_START.md"


def test_readme_mentions_governance_sandbox_result_card_download_start_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_WEB_DEMO_RESULT_CARD_DOWNLOAD_START.md" in readme
    assert "scenario-file -> result card -> report-download proof path" in readme


def test_governance_sandbox_result_card_download_start_note_keeps_narrow_lane() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "import one scenario file" in note
    assert "render one result card" in note
    assert "verify one report download action" in note
