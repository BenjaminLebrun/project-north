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

    if not 1 <= args.day <= 31:
        parser.error("Day must be between 1 and 31")

    if not 1 <= args.month <= 12:
        parser.error("Month must be between 1 and 12")

    result = generate_profile_report(
        args.name,
        args.day,
        args.month,
        args.year,
    )

    display_profile(result)


if __name__ == "__main__":
    run()