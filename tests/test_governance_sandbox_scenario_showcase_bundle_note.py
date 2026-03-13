from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_SHOWCASE_BUNDLE_NOTE.md'


def test_readme_mentions_governance_sandbox_scenario_showcase_bundle_note() -> None:
    readme = README.read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_SHOWCASE_BUNDLE_NOTE.md' in readme
    assert 'scenario_showcase' in readme


def test_governance_sandbox_scenario_showcase_bundle_note_keeps_validator_gate_visible() -> None:
    note = NOTE.read_text(encoding='utf-8')
    assert 'scenario_showcase' in note
    assert 'JSON/Markdown/HTML report bundle' in note
    assert 'validator pass' in note
