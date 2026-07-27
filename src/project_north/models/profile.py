from dataclasses import dataclass


@dataclass
class ProfileIdentity:
    name: str


@dataclass
class ProfileDate:
    day: int
    month: int
    year: int


@dataclass
class NumerologyProfile:
    identity: ProfileIdentity
    birth_date: ProfileDate
    expression: int
    soul: int
    personality: int
    life_path: int
