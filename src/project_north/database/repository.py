from project_north.database.first_names import load_first_names
from project_north.database.analyzer import analyze_first_names


def get_first_names():
    return analyze_first_names(
        load_first_names()
    )