from pathlib import Path


def test_readme_mentions_repo45_scenario_report_phase_one_pair_note() -> None:
    readme = Path(__file__).resolve().parents[1] / "README.md"
    assert "docs/VALIDATE_REPO45_SCENARIO_REPORT_PHASE_ONE_PAIR_NOTE.md" in readme.read_text(encoding="utf-8")
