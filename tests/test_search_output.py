from project_north.search.search import search_first_names


def test_search_output():

    results = search_first_names({})

    print()

    print("RANKING")

    print("-" * 40)

    for index, result in enumerate(results, start=1):

        print(
            f"{index:>2}. "
            f"{result['name']:<15} "
            f"{result['score']:>3}"
        )