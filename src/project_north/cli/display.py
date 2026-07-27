def display_profile(result):

    profile = result["profile"]
    interpretation = result["interpretation"]

    print("========================")
    print("PROJECT NORTH PROFILE")
    print("========================")

    print()

    print(f"Name: {profile['identity']['name']}")

    print()

    print("Expression:")
    print(profile["expression"]["expression"])
    print(interpretation["expression"])

    print()

    print("Soul:")
    print(profile["soul"]["soul"])
    print(interpretation["soul"])

    print()

    print("Personality:")
    print(profile["personality"]["personality"])
    print(interpretation["personality"])

    print()

    print("Life Path:")
    print(profile["birth_date"]["life_path"]["life_path"])
    print(interpretation["life_path"])