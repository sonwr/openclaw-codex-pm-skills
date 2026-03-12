from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_NOTE.md'

def test_readme_mentions_governance_sandbox_scenario_report_priority_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_REPORT_PRIORITY_NOTE.md' in readme
    assert 'scenario-file input plus markdown/html report output' in readme

def test_governance_sandbox_scenario_report_priority_note_keeps_priority_pair_visible() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'scenario file' in note
    assert 'JSON/Markdown/HTML report bundle' in note
    assert 'repositories 4 and 5 as non-optional' in note
