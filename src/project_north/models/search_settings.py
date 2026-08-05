from dataclasses import dataclass


@dataclass
class SearchSettings:

    use_biblical: bool = True
    use_historical: bool = True
    use_royal: bool = True
    use_meaning: bool = True