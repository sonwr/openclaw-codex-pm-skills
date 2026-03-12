from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_STATUS_NOTE.md'


def test_readme_mentions_governance_sandbox_scenario_file_report_status_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_FILE_REPORT_STATUS_NOTE.md' in readme
    assert 'one imported scenario file plus one generated JSON/Markdown/HTML report bundle' in readme


def test_governance_sandbox_scenario_file_report_status_note_keeps_status_scope_small() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'one imported scenario file' in note
    assert 'one generated JSON/Markdown/HTML report bundle' in note
    assert 'validator pass' in note
