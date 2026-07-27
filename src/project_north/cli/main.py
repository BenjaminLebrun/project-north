import argparse

from project_north.cli.display import display_profile
from project_north.export.exporter import export_profile
from project_north.services.profile_service import (
    generate_profile_report,
)


def run():

    parser = argparse.ArgumentParser(
        prog="project-north",
        description="Project North numerology profile engine.",
    )
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

    parser.add_argument(
        "--format",
        choices=["terminal", "json", "markdown"],
        default="terminal",
        help="Output format",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="project-north 0.2.0",
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

    if args.format == "terminal":
        display_profile(result)
    else:
        print(
            export_profile(
                result,
                args.format,
            )
        )


if __name__ == "__main__":
    run()
