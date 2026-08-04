from project_north.scoring.constitution import TARGET_PROFILE


def test_target_profile():

    assert TARGET_PROFILE["expression"] == [8, 1, 4]
    assert TARGET_PROFILE["soul"] == [33, 6]
    assert TARGET_PROFILE["personality"] == [4, 8]