from enum import Enum, IntEnum
from dataclasses import dataclass
from typing import List, Dict, Tuple, Set, Union


class Importance(IntEnum):
    HIGH = 5
    MHI = 4
    MID = 3
    MLO = 2
    LOW = 1
    NONE = 0


class Equipment(Enum):
    TREKKING_SHOES = "Trekking Shoes"
    CAMERA = "Camera"
    WATER_SHOES = "Water-proof Shoes"
    SWIMMING = "Swimming Gear"


@dataclass
class Attraction:
    name: str
    time_est: float
    things: List[Equipment]
    importance: Importance
    price: float = None

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o) -> bool:
        try:
            return self.name == o.name
        except AttributeError:
            return False


@dataclass
class Ride:
    duration: float

    def __add__(self, other):
        return Ride(self.duration + other.duration)


@dataclass
class Dataset:
    attractions: List[Attraction]
    distances: Dict[Tuple[str, str], float]
    base: Attraction


@dataclass
class Region:
    dataset: Dataset
    clusters: List[Set[Attraction]]  # By now, clusters are selected by hand


@dataclass
class Itinerary:
    steps: List[Union[Attraction, Ride]]
