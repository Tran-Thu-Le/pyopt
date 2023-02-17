import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import geopandas as gpd
from scipy.spatial import Delaunay


cities = gpd.read_file('data_germany.geo.json')
# cities = gpd.read_file('data_france.geojson')
# cities = gpd.read_file('data_vietnam.geojson')


# vetnam: https://github.com/Vizzuality/growasia_calculator/blob/master/public/vietnam.geojson
# france: https://france-geojson.gregoiredavid.fr/
# germany: https://github.com/isellsoap/deutschlandGeoJSON/blob/main/2_bundeslaender/4_niedrig.geo.json


def get_data(cities):
    cen = cities.centroid
    x = np.array(cen.x)
    y = np.array(cen.y)
    centroids = np.vstack([x, y]).T  # shape (n, 2)
    tri = Delaunay(centroids)

    edges = set()
    for simplex in tri.simplices:
        edges.add((simplex[0], simplex[1]))
        edges.add((simplex[1], simplex[2]))
        edges.add((simplex[2], simplex[0]))

    edges = [list(e) for e in edges]
    edge_lengths = []
    for e in edges:
        length = np.linalg.norm(centroids[e[0]] - centroids[e[1]])
        e.append({"len": length})
    return centroids, tri.simplices, edges


centroids, simplices, edges = get_data(cities)
pos = dict(enumerate(centroids))
G = nx.Graph()
G.add_edges_from(edges)

LONG_DISTANCE = 3
for e in G.edges:
    if G.edges[e]["len"] > LONG_DISTANCE:
        G.remove_edge(*e)
        # pass


ax = cities.plot(cmap='cool', figsize=(10, 10))
# nx.draw(G, pos, ax=ax)
nx.draw_networkx(G, pos, ax=ax,  node_size=5,
                 node_color="red", with_labels=False)
plt.show()
