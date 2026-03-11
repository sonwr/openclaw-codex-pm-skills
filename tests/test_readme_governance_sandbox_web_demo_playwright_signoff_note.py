from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTE = ROOT / "docs" / "GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_SIGNOFF_NOTE.md"


def test_readme_mentions_governance_sandbox_web_demo_playwright_signoff_note() -> None:
    readme = README.read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_WEB_DEMO_PLAYWRIGHT_SIGNOFF_NOTE.md" in readme
    assert NOTE.exists()


def test_governance_sandbox_web_demo_playwright_signoff_note_keeps_signoff_scope_small() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "one scenario source" in note
    assert "one visible result card" in note
    assert "one report artifact check" in note
