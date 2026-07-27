import argparse

from project_north.cli.display import display_profile

from project_north.services.profile_service import (
    generate_profile_report,
)


def run():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "name",
    )

    parser.add_argument(
        "day",
        type=int,
    )

    parser.add_argument(
        "month",
        type=int,
    )

    parser.add_argument(
        "year",
        type=int,
    )

    args = parser.parse_args()

    result = generate_profile_report(
        args.name,
        args.day,
        args.month,
        args.year,
    )

    display_profile(result)


if __name__ == "__main__":
    run()