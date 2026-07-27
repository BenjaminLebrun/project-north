def create_interpretation(profile):

    return {
        "core": {
            "expression": profile["expression"]["expression"],
            "soul": profile["soul"]["soul"],
            "personality": profile["personality"]["personality"],
            "life_path": profile["birth_date"]["life_path"]["life_path"],
        }
    }