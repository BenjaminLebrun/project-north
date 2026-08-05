from project_north.models.compatibility_settings import (
    CompatibilitySettings,
)


def test_default_settings():

    settings = CompatibilitySettings()

    assert settings.use_expression is True
    assert settings.use_soul is True
    assert settings.use_personality is True

    assert settings.use_biblical is True
    assert settings.use_historical is True
    assert settings.use_royal is True

    assert settings.use_meaning is True