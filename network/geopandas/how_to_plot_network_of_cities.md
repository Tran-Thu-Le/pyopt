# Using Python to plot the city graph of France

**Author:** Tran Thu Le & ChatGPT  
**Date:** 14/02/2023  
**Github:** [TranThuLe/pyopt](https://github.com/Tran-Thu-Le/pyopt) 

Here's a tutorial on how to plot the city graph of France using Python:

![](https://github.com/Tran-Thu-Le/ttl_blog/blob/main/images/france.png?raw=true)

To begin, we'll load the city data in the `geojson` format by importing the required libraries and accessing the dataset available for download at [France-geojson - Departements](https://france-geojson.gregoiredavid.fr/). The downloaded file should be saved as `france.json`.


```py 
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import geopandas as gpd
from scipy.spatial import Delaunay

cities = gpd.read_file('data_france.geojson')
```

Next, we'll define a function `get_data` that extracts the necessary data for the graph, including the centroids of each city, the simplices (triangles) of the Delaunay triangulation, and the edges of the graph:



```py
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
``` 

Now, we'll call `get_data` to obtain the necessary data for the graph and define a dictionary `pos` that maps each node index to its corresponding centroid coordinates.  Now create a `networkx.Graph` object and add the edges to it. We'll also remove edges that are too long.


```py
centroids, simplices, edges = get_data(cities)
pos = dict(enumerate(centroids))
G = nx.Graph()
G.add_edges_from(edges)
LONG_DISTANCE = 1.5
for e in G.edges:
    if G.edges[e]["len"] > LONG_DISTANCE:
        G.remove_edge(*e)
``` 

Finally, we'll plot the cities and the graph using `geopandas` and `networkx`, respectively:

```py
ax = cities.plot(cmap='cool', figsize=(10, 10))
# nx.draw(G, pos, ax=ax)
nx.draw_networkx(G, pos, ax=ax,  node_size=5,
                 node_color="red", with_labels=False)
plt.show()
``` 

This will create a plot of the cities of France with the corresponding graph overlayed on top. The nodes of the graph will be displayed as small red circles as you see at the begining of this post.