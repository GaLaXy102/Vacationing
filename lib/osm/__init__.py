from typing import Tuple, Optional

import requests as requests
from OSMPythonTools import nominatim

NOMINATIM_URL = "http://localhost:8080/"
OSRM_URL = "http://localhost:5000/"
OSRM_ROUTE_URI = "route/v1/car/"


def get_coordinates(name: str) -> Optional[Tuple[float, float]]:
    result = nominatim.Nominatim(endpoint=NOMINATIM_URL).query(name).toJSON()
    if result:
        return float(result[0]["lat"]), float(result[0]["lon"])
    return 0, 0


def get_distance(from_name: str, to_name: str) -> float:
    from_coords = get_coordinates(from_name)
    to_coords = get_coordinates(to_name)
    result = requests.get(OSRM_URL + OSRM_ROUTE_URI + "{1},{0};{3},{2}".format(*from_coords, *to_coords))
    routes = result.json()["routes"]
    return routes[0]["duration"] / 3600
