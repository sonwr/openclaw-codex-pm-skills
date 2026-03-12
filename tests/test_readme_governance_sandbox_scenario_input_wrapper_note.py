from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md'


def test_readme_mentions_governance_sandbox_scenario_input_wrapper_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_INPUT_WRAPPER_NOTE.md' in readme
    assert 'scenario_document' in readme


def test_governance_sandbox_scenario_input_wrapper_note_mentions_wrapper_aliases() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'scenario_document' in note
    assert 'scenario_manifest' in note
    assert 'proposal + stakeholder payload' in note
