from project_north.services.profile_service import (
    generate_profile_report,
)


def run():

    profile = generate_profile_report(
        "Benjamin Lebrun",
        12,
        11,
        1997,
    )

    print(profile)


if __name__ == "__main__":
    run()