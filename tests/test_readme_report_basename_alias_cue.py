from pathlib import Path


def test_readme_mentions_report_basename_alias_cue() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_REPORT_BASENAME_ALIAS_CUE.md" in readme
    assert (root / "docs" / "GOVERNANCE_SANDBOX_REPORT_BASENAME_ALIAS_CUE.md").exists()
