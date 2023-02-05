import numpy as np
import pypoman
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


def get_vertices(A, b):
    """Return vertices of the convex set defined by Ax<=

    Args:
        A (array): normal vector of shape (n, 2)
        b (array): intercepts of shape (n,)

    Return 
        vertices (array): vertices of convex set of shape (n, 2)
    """
    # find the vertices as a list
    vertices = pypoman.compute_polytope_vertices(A, b)
    # turn vertices to an array
    vertices = np.vstack(vertices)  # shape (n, 2)
    # find the order of these vertices so that its form a convex hull of itself
    indices = ConvexHull(vertices).vertices
    # rearange these vertices
    vertices = vertices[indices, :]

    return vertices


A = np.array([[0, -1], [1, 0], [0, 1], [-1, 0], [1, 1]])
b = np.array([0, 2, 1, 0, 2.5]).reshape(-1, 1)
vertices = get_vertices(A, b)
plt.fill(vertices[:, 0], vertices[:, 1], color="green",
         alpha=0.5, edgecolor='black', linewidth=3)
plt.xlim([-0.5, 2.5])
plt.ylim([-0.5, 1.5])
plt.show()
