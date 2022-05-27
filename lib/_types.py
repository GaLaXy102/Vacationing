from enum import Enum, IntEnum
from dataclasses import dataclass
from typing import List, Dict, Tuple, Set, Optional


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

    def __str__(self):
        return "+ {}".format(self.value)


@dataclass
class ItineraryStep:
    duration: float
    price: float
    equipment: Set[Equipment]


@dataclass
class Attraction(ItineraryStep):
    name: str
    importance: Importance
    coordinates: Optional[Tuple[float, float]]

    def __init__(self, name: str, duration: float, equipment: Set[Equipment], importance: Importance,
                 price: float = None, coordinates: Optional[Tuple[float, float]] = None):
        super(Attraction, self).__init__(duration, price, equipment)
        self.name = name
        self.importance = importance
        self.coordinates = coordinates

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o) -> bool:
        try:
            return self.name == o.name
        except AttributeError:
            return False

    def __str__(self):
        return "> A {}".format(self.name)


@dataclass
class Ride(ItineraryStep):

    def __init__(self, duration: float):
        super(Ride, self).__init__(duration, None, {})

    def __str__(self):
        return "> R {:.2f} h".format(self.duration)


@dataclass
class Dataset:
    attractions: frozenset[Attraction]
    distances: Dict[Tuple[str, str], float]
    base: Attraction


@dataclass
class Region:
    dataset: Dataset
    clusters: Set[frozenset[Attraction]]  # By now, clusters are selected by hand


@dataclass
class Itinerary:
    steps: List[ItineraryStep]

    def __iter__(self):
        return iter(self.steps)

    def __str__(self):
        equipment = set()
        for step in self:
            for eq in step.equipment:
                equipment.add(eq)
        return ("Steps:\n"
                "{}\n"
                "\n"
                "Duration : {:5.2f} h\n"
                "Cost     : {:5.2f} €\n"
                "Equipment:\n"
                "{}").format(
            "\n".join(str(x) for x in self),
            sum(x.duration for x in self),
            sum(x.price or 0 for x in self),
            "\n".join(str(x) for x in equipment)
        )
