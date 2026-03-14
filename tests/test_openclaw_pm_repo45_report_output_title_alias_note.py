from pathlib import Path


def test_readme_mentions_report_output_title_alias_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "OPENCLAW_PM_REPO45_REPORT_OUTPUT_TITLE_ALIAS_NOTE.md" in readme


def test_note_mentions_report_output_title_alias() -> None:
    note = Path("docs/OPENCLAW_PM_REPO45_REPORT_OUTPUT_TITLE_ALIAS_NOTE.md").read_text(encoding="utf-8")
    assert "report_output_title" in note
    assert "repo 4" in note and "repo 5" in note
