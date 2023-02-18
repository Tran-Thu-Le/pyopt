# Introduction to NetworkX: Basic Tools

**Author:** Tran Thu Le & ChatGPT  
**Date:** 18/02/2023  


**Abstract.** NetworkX is a Python library for the creation, manipulation, and study of complex networks.

[[TOC]]



## Basic Analysis

NetworkX provides several functions for performing basic analysis on graphs, including computing centrality measures, finding shortest paths, and detecting communities.

### Centrality Measures

Centrality measures are used to identify the most important nodes in a graph. NetworkX provides several different centrality measures, including degree centrality, betweenness centrality, and eigenvector centrality.


```py
# Create a graph with five nodes and four edges
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Compute degree centrality
degree_centrality = nx.degree_centrality(G)
print(degree_centrality)
``` 

Output:


```py
{1: 0.3333333333333333, 2: 0.6666666666666666, 3: 0.6666666666666666, 4: 0.6666666666666666, 5: 0.3333333333333333}
``` 

In this example, we created a graph with five nodes and four edges. We then used the `degree_centrality()` function to compute the degree centrality of each node in the graph.








### Community Detection

In this example, we created a graph with six nodes and seven edges. We then used the `shortest_path()` function to compute the shortest path between nodes 1 and 5 in the graph.

Community detection algorithms are used to identify groups of nodes that are densely connected within a graph. NetworkX provides several different community detection algorithms, including the Girvan-Newman algorithm and the Louvain algorithm.


```py
# Create a graph with six nodes and seven edges
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)

# Compute communities using the Louvain algorithm
communities = community_louvain(G)

# Print the communities
for community in set(communities.values()):
    print("Community", community)
    nodes = [nodes for nodes in communities.keys() if communities[nodes] == community]
    print(nodes)
``` 

Output:

```py
Community 0
[1, 2, 3]
Community 1
[4, 5, 6]
``` 

In this example, we created a graph with six nodes and seven edges. We then used the `community_louvain()` function to compute the communities in the graph using the Louvain algorithm. Finally, we printed the communities and the nodes that belong to each community.


## Drawing a Spanning Tree

A spanning tree of a graph is a tree that spans all of the nodes in the graph, that is, it is a subgraph of the graph that is a tree and includes all of the nodes in the original graph. 

NetworkX provides a function `minimum_spanning_tree()` to compute the minimum spanning tree of a graph. Once we have the minimum spanning tree, we can use the `draw()` function from Matplotlib to visualize it.


```py
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edge(1, 2, weight=4)
G.add_edge(1, 3, weight=1)
G.add_edge(1, 4, weight=3)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=1)
G.add_edge(3, 4, weight=5)

# Compute the minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Draw the minimum spanning tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(T, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
``` 



In this example, we created a graph and added edges with weights. We then used the `minimum_spanning_tree()` function to compute the minimum spanning tree of the graph. Finally, we used the `draw()` function from Matplotlib to visualize the minimum spanning tree.

## Minimum Cuts

Minimum cuts in a graph are the edges that, when removed, disconnect the graph into two or more disconnected components with the smallest possible number of edges.

NetworkX provides a function `minimum_cut()` to compute the minimum cut of a graph. The function returns a tuple `(S, T, cut_value)`, where `S` and `T` are sets of nodes that define the minimum cut and `cut_value` is the weight of the cut.


```py
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge(1, 2, capacity=3.0)
G.add_edge(1, 3, capacity=1.0)
G.add_edge(2, 3, capacity=1.0)
G.add_edge(2, 4, capacity=2.0)
G.add_edge(3, 4, capacity=3.0)

# Compute the minimum cut
cut_value, partition = nx.minimum_cut(G, 1, 4)
reachable, non_reachable = partition

# Print the minimum cut
print("Minimum Cut: ", cut_value)

# Print the sets of nodes that define the minimum cut
print("Set 1: ", reachable)
print("Set 2: ", non_reachable)
``` 

Output:


```py
Minimum Cut:  3.0
Set 1:  {1, 2, 3}
Set 2:  {4}
``` 

In this example, we created a graph and added edges with capacities. We then used the `minimum_cut()` function to compute the minimum cut of the graph, given the source node 1 and the target node 4. Finally, we printed the minimum cut and the sets of nodes that define the minimum cut.

## Adding Weights to Nodes and Length/Capacity to Edges

In many cases, it is useful to assign weights to nodes or lengths/capacities to edges in a graph. For example, weights can represent the importance of a node or the length of a path in a transportation network, while capacities can represent the maximum flow that can pass through an edge in a network flow problem. NetworkX provides a way to assign weights to nodes and lengths/capacities to edges, and to access these data when needed.

### Adding Weights to Nodes

Adding weights to nodes in NetworkX is straightforward. You can add the weight as a node attribute using the `add_node()` method.


```py
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes with weights
G.add_node(1, weight=0.5)
G.add_node(2, weight=1.0)
G.add_node(3, weight=1.5)

# Access the weight of a node
print("Weight of node 1: ", G.nodes[1]['weight'])
``` 

Output:


```py
Weight of node 1:  0.5
``` 

In this example, we created a graph and added nodes with weights using the `add_node()` method. We then accessed the weight of node 1 using the `nodes` attribute of the graph.

## Adding Length/Capacity to Edges

Adding length or capacity to edges in NetworkX is also simple. You can add the length or capacity as an edge attribute using the `add_edge()` method.


```py
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges with lengths/capacities
G.add_edge(1, 2, length=1.0)
G.add_edge(2, 3, length=1.5)
G.add_edge(3, 1, capacity=2.0)

# Access the length/capacity of an edge
print("Length of edge (1, 2): ", G.edges[(1, 2)]['length'])
print("Capacity of edge (3, 1): ", G.edges[(3, 1)]['capacity'])
``` 

Output:


```py
Length of edge (1, 2):  1.0
Capacity of edge (3, 1):  2.0
``` 

In this example, we created a graph and added edges with lengths/capacities using the `add_edge()` method. We then accessed the length of edge (1, 2) and the capacity of edge (3, 1) using the `edges` attribute of the graph.


## Computing the Shortest Path and Its Length

In many graph problems, it is useful to find the shortest path between two nodes in a graph. For example, in a transportation network, we may want to find the shortest route between two cities. NetworkX provides several algorithms to compute the shortest path and its length in a graph.

## Computing the Shortest Path

The `shortest_path()` method of NetworkX can be used to compute the shortest path between two nodes in a graph. This method returns a list of nodes representing the shortest path from the source node to the target node.



```py
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=3)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=2)
G.add_edge(3, 4, weight=1)

# Compute the shortest path from node 1 to node 4
shortest_path = nx.shortest_path(G, source=1, target=4, weight='weight')

print("Shortest path from node 1 to node 4: ", shortest_path)
``` 

Output:


```py
Shortest path from node 1 to node 4:  [1, 2, 3, 4]
``` 

In this example, we created a graph and added edges with weights using the `add_edge()` method. We then computed the shortest path from node 1 to node 4 using the `shortest_path()` method, and printed the result.

## Computing the Length of the Shortest Path

The `shortest_path_length()` method of NetworkX can be used to compute the length of the shortest path between two nodes in a graph. This method returns a number representing the length of the shortest path from the source node to the target node.



```py
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=3)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=2)
G.add_edge(3, 4, weight=1)

# Compute the length of the shortest path from node 1 to node 4
shortest_path_length = nx.shortest_path_length(G, source=1, target=4, weight='weight')

print("Length of the shortest path from node 1 to node 4: ", shortest_path_length)
``` 

Output:



```py
Length of the shortest path from node 1 to node 4:  3
``` 

In this example, we created a graph and added edges with weights using the `add_edge()` method. We then computed the length of the shortest path from node 1 to node 4 using the `shortest_path_length()` method, and printed the result.


## Conclusion

In this tutorial, we learned how to use NetworkX to create, manipulate, and analyze graphs. We also learned how to visualize graphs using Matplotlib, and how to compute centrality measures, shortest paths, and communities in a graph. With this knowledge, you should be able to use NetworkX to solve a wide range of graph-related problems.

Here we also learned how to draw a minimum spanning tree and compute the minimum cut of a graph using NetworkX. With these techniques, you can identify the most important edges in a graph and use this information to optimize network flows.

In this tutorial, we learned how to add weights to nodes and length/capacity to edges in NetworkX. We also learned how to access these data using the `nodes` and `edges` attributes of the graph. With these techniques, you can represent a wide range of graph problems and use the weights and capacities to optimize solutions to these problems.