import matplotlib.figure
import matplotlib.pyplot as plt
from typing import Tuple


from ._types import Importance, Dataset
from .osm import get_coordinates


color_by_importance = {
    Importance.HIGH: "red",
    Importance.MHI: "orange",
    Importance.MID: "yellow",
    Importance.MLO: "darkgreen",
    Importance.LOW: "lightgreen",
    Importance.NONE: "gray"
}

"""
def get_graph(dataset: Dataset,
              min_importance: Importance = Importance.NONE) -> networkx.Graph:
    v = [(a.name, {"imp": a.importance})
         for a in dataset.attractions if a.importance >= min_importance or a == dataset.base]
    e = [(k[0], k[1], 1 / v) for k, v in dataset.distances.items()]
    g = networkx.Graph()
    g.add_nodes_from(v, data=True)
    g.add_weighted_edges_from(e)
    return g


def draw_graph(dataset: Dataset, min_importance: Importance,
               size: Tuple[int, int], seed: int) -> matplotlib.figure.Figure:
    fig: matplotlib.figure.Figure
    fig = plt.figure(figsize=size)
    ax = fig.add_subplot()
    g = get_graph(dataset, min_importance)
    pos = networkx.spring_layout(g, seed=seed)
    colors = [color_by_importance[n[1]] for n in g.nodes(data="imp")]
    labels = {n: "{}\n{:1.1f}".format(n, get_attraction_by_name(n, dataset.attractions).duration) for n in g.nodes}
    edge_labels = {e: "{:1.1f}".format(1/g.get_edge_data(*e)["weight"]) for e in g.edges}
    networkx.draw(g, pos, ax=ax, with_labels=True, labels=labels, node_color=colors)
    networkx.draw_networkx_edge_labels(g, pos, ax=ax, edge_labels=edge_labels)
    return fig
"""


def draw_graph(dataset: Dataset, min_importance: Importance,
               size: Tuple[int, int], seed: int = None) -> matplotlib.figure.Figure:
    ds_with_imp = [x for x in dataset.attractions if x.importance >= min_importance]
    coords = list(map(list, zip(*[x.coordinates or get_coordinates(x.name) for x in ds_with_imp])))
    colors = [color_by_importance[x.importance] for x in ds_with_imp]
    labels = ["{}\n{:1.1f}".format(x.name, x.duration) for x in ds_with_imp]
    fig: matplotlib.figure.Figure = plt.figure(figsize=size)
    ax: matplotlib.figure.Axes = fig.add_subplot()
    ax.scatter(
        x=coords[1],
        y=coords[0],
        c=colors
    )
    for idx in range(len(ds_with_imp)):
        ax.annotate(
            text=labels[idx],
            xy=(coords[1][idx], coords[0][idx])
        )
    return fig
