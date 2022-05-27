from typing import Tuple, Optional

from OSMPythonTools import nominatim

NOMINATIM_URL = "http://localhost:8080/"


def get_coordinates(name: str) -> Optional[Tuple[float, float]]:
    result = nominatim.Nominatim(endpoint=NOMINATIM_URL).query(name).toJSON()
    if result:
        return float(result[0]["lat"]), float(result[0]["lon"])
    return 0, 0
