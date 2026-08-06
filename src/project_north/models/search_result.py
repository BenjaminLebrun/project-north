# from dataclasses import dataclass, field

from dataclasses import dataclass

@dataclass
class SearchResult:
    rank: int
    name: str

    expression: int
    soul: int
    personality: int

    match_percentage: float

    interpretation: str

    biblical: bool
    historical: bool
    royal: bool

    origin: str
    meaning: str


    score: int

    base_score: int = 0
    bonus_score: int = 0

    # details: list[str] = field(default_factory=list)