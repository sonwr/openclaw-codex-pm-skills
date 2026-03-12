from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_FIVE_REPO_ACTIVE_SLICE_NOTE.md'

def test_readme_mentions_governance_sandbox_five_repo_active_slice_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_FIVE_REPO_ACTIVE_SLICE_NOTE.md' in readme
    assert 'all five active repos' in readme

def test_governance_sandbox_five_repo_active_slice_note_keeps_governance_priority_visible() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'five active repos' in note
    assert 'scenario-file/report-first' in note
    assert 'repositories 4 and 5 as non-optional' in note
