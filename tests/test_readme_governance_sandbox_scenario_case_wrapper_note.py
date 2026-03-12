from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / 'docs' / 'GOVERNANCE_SANDBOX_SCENARIO_CASE_WRAPPER_NOTE.md'


def test_readme_mentions_governance_sandbox_scenario_case_wrapper_note() -> None:
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    assert 'docs/GOVERNANCE_SANDBOX_SCENARIO_CASE_WRAPPER_NOTE.md' in readme
    assert NOTE.exists()
