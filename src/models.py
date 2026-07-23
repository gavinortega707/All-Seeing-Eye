from dataclasses import dataclass

@dataclass
class Event:
    venue: str
    date: str
    time: str
    price: str
    bands: list[str]
    genres: list[str]