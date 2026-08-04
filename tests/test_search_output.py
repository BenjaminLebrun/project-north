from project_north.search.search import search_first_names
from project_north.models.search_profile import SearchProfile

def test_search_output():

    profile = SearchProfile(
    expression=5,
    soul=5,
    personality=9,
    life_path=22,
)

    results = search_first_names(profile)

    print()

    print("RANKING")

    print("-" * 40)

    for index, result in enumerate(results, start=1):

        print(
            f"{index:>2}. "
            f"{result.name:<15} "
            f"{result.score:>3} "
            f"- {result.interpretation}"
        )

        for detail in result.details:
            print(f"      - {detail}")