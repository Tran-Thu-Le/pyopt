# Linear Programming using Interior Point Method 

Linear programming is a method to optimize a linear objective function subject to linear constraints. The interior point method is an algorithm that can be used to solve linear programming problems by moving a point inside the feasible set.

## Problem Statement
Consider the following linear programming problem:

$$\min_{x \in \mathbb{R}^n} c^T x$$

subject to

$$Ax≤b$$

where $c \in \mathbb{R}^n$, $A \in \mathbb{R}^{m \times n}$, and $b \in \mathbb{R}^m$.

## Barrier Function
To use the interior point method, we need to define a barrier function that penalizes violation of the constraints. The convex barrier function $-\log$ is frequently used:

$$\phi(x) = - \sum_{i=1}^m \log (b_i - a_i^T x)$$

where $a_i^T$ is the $i$-th row of $A$.

The barrier function approaches infinity as $x$ approaches the boundary of the feasible region. Therefore, minimizing the barrier function ensures that $x$ stays inside the feasible region.

## Interior Point Method
The interior point method solves the following optimization problem:

$$\min_{x \in \mathbb{R}^n} c^T x + \frac{1}{t}\phi(x)$$

where $t$ is a positive scalar called the barrier parameter.

The interior point method finds $x$ for an increasing sequence of $t$, until convergence. At each iteration, it solves the above optimization problem (with a specific $t$) using Newton's method.

## Python Implementation
Here's the Python code for solving the above linear programming problem using the interior point method. The produced figure is.

<img src="https://github.com/Tran-Thu-Le/ttl_blog/blob/main/images/interior_point_method.png?raw=true" alt="Interior point method" width="70%">


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pypoman
from scipy.spatial import ConvexHull

# Define the objective function
c = np.array([-1, 0])  # coefficient of decision variables in the objective function

# Define the inequality constraints
A = np.array([[1, 2], [1, -1], [-1, 1], [-1, -1]])
b = np.array([2, 2, 2, 1])

# Define the function to be minimized
def objective(x):
    return np.dot(c, x)  # minimize c'x

# Define the barrier function and its Jacobian
def barrier(x):
    return -np.sum(np.log(b - np.dot(A, x)))

def jacobian_barrier(x):
    return np.dot(A.T, (1/ (b-A.dot(x))))

# Define the function to be minimized for the interior point method
def func_to_minimize(x, t):
    return objective(x) + barrier(x)/t

def jacobian_func(x, t):
    return c + jacobian_barrier(x)/t

# data container for x and t
x0 = np.array([0, 0])
x = x0
t = 1
x_list = [x]
t_list = [t]

# Implement the interior point method
for i in range(10):
    # Define the function to be minimized and its Jacobian
    func = lambda x: func_to_minimize(x, t)
    jac = lambda x: jacobian_func(x, t)
    
    # Solve the optimization problem
    res = minimize(func, x, method='Newton-CG', jac=jac)
    print(f"Iter={i}, success={res.success}, gap={2/t}")
    
    # Update t and x0
    t *= 1.8
    x = res.x.copy()
    t_list += [t]
    x_list += [x]
```

We the plot the figure

```python
# Plot the movement of the solution point
fig, ax = plt.subplots()
vertices = pypoman.compute_polytope_vertices(A, b)
vertices = np.vstack(vertices) # shape (n, 2)
indices = ConvexHull(vertices).vertices
vertices = vertices[indices, :]

delta = 0.025
x_grid = np.arange(-2.0, 2.5, delta)
y_grid = np.arange(-2.0, 1.5, delta)
X, Y = np.meshgrid(x_grid, y_grid)
Z = np.zeros_like(X)


x_list = np.array(x_list)
levels = np.sort([func_to_minimize(x, t) for x, t in zip(x_list, t_list)])

def plot_contour(point, t):	
	for i in range(len(x_grid)):
		for j in range(len(y_grid)):
			Z[j, i] = func_to_minimize([x_grid[i], y_grid[j]], t)
	lev = [func_to_minimize(point, t)]
	ax.contour(X, Y, Z, levels=lev, colors='black', linewidths=1)
        
for point, t in zip(x_list, t_list):
    plot_contour(point, t)

ax.fill(vertices[:, 0], vertices[:, 1], color="cyan",
         alpha=0.3, edgecolor='black', linewidth=1)
ax.set_xlim([-2, 2.5])
ax.set_ylim([-2, 1.5])
ax.plot(x_list[:, 0], x_list[:, 1], 'o--', markersize=5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Interior Point Method for Linear Programming')
plt.show()
```





