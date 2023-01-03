import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def conditional_gradient(A, b, c, x_init,
                         alpha=1e-2, iter_stop=100, eps_stop=1e-6):
    """Conditional gradient method (Frank-Wolfe)

        Here we want to solve:

        min_{x} 1/2 * ||x-c||^2 
        s.t. Ax<=b

        By approximating the objective function by its linearization at current position xk,
        we have

        f(x) ~ f(xk) + <grad(xk), x-xk>

        Thus, we can update x using the solution of the following linear approximation
        min_{x} <v,x>
        s.t. Ax<=b

        where v=x-c is the gradient of f.


        Note: This linear programming problem 
        can be solved using scipy.optimize.linprog.
        To know how to use `scipy.optimize.linprog`: see
        1. https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
        2. https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult
    """
    x = x_init
    x_list = []
    for i in range(10):

        grad = x-c
        # print("grad", grad)
        result = linprog(grad.reshape(1, 2), A_ub=A, b_ub=b)
        x = result.x.reshape(2, 1)

        # print(f"x={x}")

        x_list += [x]
    return x, x_list


def main():
    """
        A: m x n
        x: n x 1 
        b: m x 1
        Ax <= b

        f(x)= ||x-c||^2
    """
    c = np.array([2, 2]).reshape(2, 1)
    A = np.array([[1, 0], [0, 1]])
    b = np.array([1, 1]).reshape(2, 1)
    x_init = np.array([1, 0]).reshape(2, 1)

    # print(x_init)
    # print(b)

    x_opt, x_list = conditional_gradient(A, b, c, x_init)

    # print(x_list)
    print(x_opt)


main()
