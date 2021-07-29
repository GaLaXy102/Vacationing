from ._types import Attraction
from typing import Dict, Tuple


def get_attraction_by_name(name: str, attractions: frozenset[Attraction]) -> Attraction:
    # Search by name
    for a in attractions:
        if a.name == name:
            return a


def get_distance(start: Attraction, end: Attraction,
                 distance_map: Dict[Tuple, float], default=1000) -> float:
    if (start.name, end.name) in distance_map.keys():
        return distance_map[(start.name, end.name)]
    elif (end.name, start.name) in distance_map.keys():
        return distance_map[(end.name, start.name)]
    else:
        return default
