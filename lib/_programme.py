from ._types import Region, Ride, Itinerary
from ._retrieve import get_distance
from typing import List


def get_itineraries(region: Region) -> List[Itinerary]:
    out = []
    for cluster in region.clusters:
        next_node = region.dataset.base, 0
        itinerary = Itinerary([next_node[0]])
        # We want a long first distance, shortest possible intermediate steps and a shorter last distance
        while cluster:
            next_node = sorted(
                [(a, get_distance(next_node[0], a, region.dataset.distances,
                                  -1 if next_node[0] == region.dataset.base else 1000))
                 for a in cluster],
                # We must handle reverse correctly when there is no edge
                key=lambda dist: dist[1], reverse=next_node[0] == region.dataset.base
            )[0]
            itinerary.steps.append(Ride(next_node[1]))
            itinerary.steps.append(next_node[0])
            cluster.remove(next_node[0])
        itinerary.steps.append(Ride(get_distance(next_node[0], region.dataset.base, region.dataset.distances)))
        itinerary.steps.append(region.dataset.base)
        out.append(itinerary)
    return out
