###########

import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

# %matplotlib notebook

plt.close('all')

fun = lambda x, y: 4 * x ** 2 + y ** 2

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-7, 7, 0.25)
Y = np.arange(-7, 7, 0.25)
X, Y = np.meshgrid(X, Y)
Z = fun(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0.01, antialiased=True, alpha=0.3)


#####################################

def step_gradient_2d(x_current, y_current, learningRate):
    x_gradient = 8 * x_current
    y_gradient = 2 * y_current

    new_x = x_current - (learningRate * x_gradient)
    new_y = y_current - (learningRate * y_gradient)

    ax.quiver(x_current, y_current, (fun(x_current, y_current)),
              - (learningRate * x_gradient), - (learningRate * y_gradient),
              (-(fun(x_current, y_current) - fun(new_x, new_y))))

    return [new_x, new_y]


def gradient_descent_runner_2d(starting_x, starting_y, learning_rate, num_iterations):
    x = starting_x
    y = starting_y
    for i in range(num_iterations):
        x, y = step_gradient_2d(x, y, learning_rate)
        # print(x, y)
    return [x, y]


learning_rate = 0.9
initial_x = 0  # initial y-intercept guess
initial_y = 5  # initial slope guess
num_iterations = 10
[x, y] = gradient_descent_runner_2d(initial_x, initial_y, learning_rate, num_iterations)

#####################################

plt.plot([initial_x], [initial_y], [fun(initial_x, initial_y)], "ok")
plt.show()