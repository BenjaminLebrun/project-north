from csv import DictReader
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "first_names.csv"
)


def load_first_names():

    with DATA_FILE.open(
        encoding="utf-8",
        newline="",
    ) as file:
        return list(DictReader(file))
        