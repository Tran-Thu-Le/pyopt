import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm, det, inv
from numpy import pi

# A small constant to check for the near-zero values
EPSILON = 1e-6


def find_max_neg_min_pos(values):
    """
    Given a list of values, returns the indices of the maximum negative value and the minimum positive value.
    """
    n = len(values)
    indices = np.arange(n)
    neg = [indices[i] for i in range(n) if values[i] < 0]
    pos = [indices[i] for i in range(n) if values[i] > 0]
    max_neg = neg[np.argmax(values[neg])]
    min_pos = pos[np.argmin(values[pos])]
    return max_neg, min_pos


def ccw(A, B, C):
    """
    Returns True if C is counter-clockwise from A to B, False otherwise.
    """
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])


def intersection(line1, line2):
    """
    Given two lines in the form of (normal_vector, intercept), returns their intersection point.
    """
    n1, b1 = line1
    n2, b2 = line2
    assert n1.shape == n2.shape == (2, )
    A = np.vstack([n1, n2])
    b = np.array([b1, b2]).reshape(-1, 1)

    assert b.shape == (2, 1)
    if np.abs(det(A) - 0) > EPSILON:
        return (inv(A) @ b).reshape(-1)
    else:
        return None


def angles(vectors, current_vector):
    """
    Given a list of 2D vectors and a current vector, returns the difference in angle (in degrees)
    between the current vector and all the other vectors.
    """
    current_angle = np.arctan2(*current_vector)
    angles = np.array([np.arctan2(*v) for v in vectors])
    diff_angles = (current_angle - angles)/pi*180
    diff_angles = ((diff_angles + 180) % 360) - 180
    return diff_angles


def find_vertices(A, b):
    # A of shape (n, 2) and b of shape (n,1)
    n, d = A.shape
    # Check if the number of columns in A is equal to 2
    assert d == 2
    # Check if the shape of b is (n, 1)
    assert b.shape == (n, 1)
    indices = np.arange(n)
    # Normalize the inequalities
    norms = np.linalg.norm(A, axis=1).reshape(-1, 1)
    A = A / norms
    b = b / norms
    vertices = []
    i = 0
    for _ in range(n):
        # Get the normal vector of the line_i
        ni = A[i, :]
        # Get the normal vectors of all other inequalities
        other_vectors = np.delete(A, i, axis=0)
        other_indices = np.delete(indices, i)
        assert other_vectors.shape == (n-1, 2)
        angle_list = angles(other_vectors, ni)
        # Find the indices of the maximum negative angle and minimum positive angle
        max_neg_index, min_pos_index = other_indices[list(
            find_max_neg_min_pos(angle_list))]
        # Get the line parameters for the max_neg_index, i, and min_pos_index
        line_a = (A[max_neg_index, :], b[max_neg_index])
        line_b = (A[i, :], b[i])
        line_c = (A[min_pos_index], b[min_pos_index])
        # Calculate the intersection points between line_a and line_b, line_b and line_c, and line_c and line_a
        pc = intersection(line_a, line_b)
        pa = intersection(line_b, line_c)
        pb = intersection(line_c, line_a)
        # If the list of vertices is empty, add pc and pa to the list of vertices
        if len(vertices) == 0:
            vertices += [pc, pa]
        # If pb is None, add pa to the list of vertices
        elif pb is None:
            vertices += [pa]
        # If pb is not None, check if pa, pb, and pc form a counterclockwise triangle
        elif not ccw(pa, pb, pc):
            vertices += [pa]
        # If the triangle is not counterclockwise, print a message
        else:
            raise Exception("Please check the source codde.")
        # update line_i
        i = min_pos_index
    return vertices


def plot_convex_set(A, b, xmin=None, xmax=None, ymin=None, ymax=None,
                    border_color="black", background_color="green"):
    """
        Plot the convex set defined by inequalities `Ax <= b`
    """
    n, d = A.shape
    assert d == 2 and b.shape == (n, 1)

    vectors = []
    intercepts = []
    if xmin is not None:
        vectors += [(-1, 0)]
        intercepts += [-xmin]
    if xmax is not None:
        vectors += [(1, 0)]
        intercepts += [xmax]
    if ymin is not None:
        vectors += [(0, -1)]
        intercepts += [-ymin]
    if ymax is not None:
        vectors += [(0, 1)]
        intercepts += [ymax]

    vectors = np.array(vectors)
    intercepts = np.array(intercepts).reshape(-1, 1)

    A_new = np.vstack([A, vectors])
    b_new = np.vstack([b, intercepts])

    nodes = find_vertices(A_new, b_new)
    nodes_x = [node[0] for node in nodes]
    nodes_y = [node[1] for node in nodes]
    plt.plot(nodes_x, nodes_y, c=border_color, lw=2)
    plt.fill(nodes_x, nodes_y, c=background_color, alpha=0.5)
    plt.xlim([xmin, xmax])
    plt.ylim([xmin, xmax])


if __name__ == "__main__":
    A = np.array([[0, -1], [1, 0], [0, 1], [-1, 0], [1, 1]])
    b = np.array([0, 2, 1, 0, 2.5]).reshape(-1, 1)
    plt.figure(1, (5, 5))
    plot_convex_set(A, b, xmin=0, xmax=3, ymin=0, ymax=3)
    plt.xlim([-0.5, 2.5])
    plt.ylim([-0.5, 1.5])
    plt.show()
