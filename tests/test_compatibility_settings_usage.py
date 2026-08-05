from project_north.compatibility.engine import evaluate_first_name
from project_north.models.compatibility_settings import (
    CompatibilitySettings,
)
from project_north.database.analyzer import analyze_first_name


def test_disable_biblical_bonus():

    first_name = analyze_first_name(
        {
            "name": "Samuel",
            "origin": "Hebrew",
            "meaning": "God has heard",
            "biblical": "true",
            "historical": "true",
            "royal": "false",
        }
    )

    settings = CompatibilitySettings(
        use_biblical=False,
    )

    result = evaluate_first_name(
        first_name,
        settings=settings,
    )

    assert "Biblique : +10" not in result["details"]

def test_disable_historical_bonus():

    first_name = analyze_first_name(
        {
            "name": "Samuel",
            "origin": "Hebrew",
            "meaning": "God has heard",
            "biblical": "true",
            "historical": "true",
            "royal": "false",
        }
    )

    settings = CompatibilitySettings(
        use_historical=False,
    )

    result = evaluate_first_name(
        first_name,
        settings=settings,
    )

    assert "Historique : +5" not in result["details"]


def test_disable_all_metadata():

    first_name = analyze_first_name(
        {
            "name": "Samuel",
            "origin": "Hebrew",
            "meaning": "God has heard",
            "biblical": "true",
            "historical": "true",
            "royal": "false",
        }
    )

    settings = CompatibilitySettings(
        use_biblical=False,
        use_historical=False,
        use_meaning=False,
    )

    result = evaluate_first_name(
        first_name,
        settings=settings,
    )

    assert all(
        "Biblique" not in detail
        for detail in result["details"]
    )

    assert all(
        "Historique" not in detail
        for detail in result["details"]
    )

    assert all(
        "Signification" not in detail
        for detail in result["details"]
    )