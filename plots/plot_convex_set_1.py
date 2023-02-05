import numpy as np
import matplotlib.pyplot as plt


def draw_regions(A, b, xlim, ylim):
    """
    Draw a 2D region defined by Ax <= b
    """
    # setup parameters
    nx, ny = 90, 80
    x = np.linspace(xlim[0], xlim[1], nx)
    y = np.linspace(ylim[0], ylim[1], ny)
    X, Y = np.meshgrid(x, y)
    gx, gy = X.reshape(-1), Y.reshape(-1)
    points = np.vstack([gx, gy])

    # find the active/feasible region
    active = (b.reshape(-1, 1) - A @ points >= 0)
    active = active.all(axis=0)
    active = active.reshape(ny, nx)

    # plot region
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.contourf(X, Y, active)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    plt.show()


if __name__ == "__main__":
    A = np.array([[0, -1], [1, 0], [0, 1], [-1, 0], [1, 1]])
    b = np.array([0, 2, 1, 0, 2.5]).reshape(-1, 1)
    draw_regions(A, b, xlim=[-0.5, 2.5], ylim=[-0.5, 1.5])
