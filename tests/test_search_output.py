from project_north.search.search import search_first_names


def test_search_output():

    results = search_first_names(
    {
        "expression": 5,
        "soul": 5,
        "personality": 9,
        "life_path": 22,
    }
    )

    print()

    print("RANKING")

    print("-" * 40)

    for index, result in enumerate(results, start=1):

        print(
            f"{index:>2}. "
            f"{result['name']:<15} "
            f"{result['score']:>3}"
        )