from pathlib import Path


def test_readme_mentions_report_output_label_alias_note() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")

    assert "docs/GOVERNANCE_SANDBOX_REPORT_OUTPUT_LABEL_ALIAS_NOTE.md" in readme
