# Introduction to NetworkX: Data Structures

**Author:** Tran Thu Le & ChatGPT  
**Date:** 18/02/2023  


**Abstract.** NetworkX is a Python library for the creation, manipulation, and study of complex networks. It is a powerful tool for exploring and analyzing large graphs and networks, and is widely used in scientific computing, data analysis, and machine learning. In this tutorial, we will cover the basics of using NetworkX, including how to create and manipulate graphs, how to visualize graphs, and how to perform basic graph analysis.

[[TOC]]

## Installation

To install NetworkX, you can use pip from the computer terminal, the Python package installer:


```bash
pip install networkx
``` 

In the case of using Google Colab, we should use

```bash
!pip install networkx
``` 


Once you have installed NetworkX, you can import it into your Python code using the following command:


```py
import networkx as nx
``` 

## Creating a Graph

The first step in using NetworkX is to create a graph. NetworkX provides several different types of graphs, including directed graphs, undirected graphs, and multigraphs. In this tutorial, we will focus on undirected graphs.

Steps to create an undirected graph in NetworkX:
1. Create a graph using the `Graph()` function.
2. Add nodes and edges to the graph using the `add_node()` and `add_edge()` functions
3. To visualize a graph in NetworkX, you can use the `draw()` function. This function takes a graph as input and draws it using the specified layout.


NetworkX provides several different ways to visualize graphs, including Matplotlib, Graphviz, and Bokeh. In this tutorial, we will focus on using Matplotlib to visualize graphs.




```py
# create graph 
G = nx.Graph()

# add nodes and edges
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# plot the graph
import matplotlib.pyplot as plt
pos = nx.spring_layout(G) # define spring layout
nx.draw(G, pos, with_labels=True)
plt.show()
```

## Data Structures

NetworkX provides several different data structures for representing graphs, including
- adjacency lists
- adjacency matrices,
- edge lists.

The choice of data structure depends on the *size* of the graph and the *type* of analysis you will be performing.

### Adjacency List

An adjacency list is a list of lists that represents the edges of a graph. Each element of the list represents a node in the graph, and the corresponding sublist contains the nodes that are adjacent to it.


```py
# Create a graph with three nodes and two edges
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Get the adjacency list of the graph
adj_list = nx.generate_adjlist(G)
print(list(adj_list))
``` 

Output:


```py
['1 2', '2 3', '']
```

In this example, we created a graph with three nodes and two edges. We then used the `generate_adjlist()` function to get the adjacency list of the graph.

### Adjacency Matrix

An adjacency matrix is a matrix that represents the edges of a graph. The rows and columns of the matrix represent the nodes in the graph, and the entries in the matrix represent the edges between the nodes.



```py
# Create a graph with three nodes and two edges
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Get the adjacency matrix of the graph
adj_matrix = nx.adjacency_matrix(G)
print(adj_matrix.todense())
``` 

Output:


```py
[[0 1 0]
 [1 0 1]
 [0 1 0]]
 ``` 

In this example, we created a graph with three nodes and two edges. We then used the `adjacency_matrix()` function to get the adjacency matrix of the graph.

### Edge List

An edge list is a list of tuples that represents the edges of a graph. Each tuple contains the two nodes that are connected by the edge.


```py
# Create a graph with three nodes and two edges
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Get the edge list of the graph
edge_list = nx.generate_edgelist(G)
print(list(edge_list))
``` 

Output:



```py
['1 2 {}', '2 3 {}']
``` 

In this example, we created a graph with three nodes and two edges. We then used the `generate_edgelist()` function to get the edge list of the graph.


 


