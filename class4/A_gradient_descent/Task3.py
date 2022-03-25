import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

f = lambda x, y: (x ** 2 - y ** 2)


def plot2d(ax):
    x = np.arange(-10, 10, 0.02)
    y = np.arange(-10, 10, 0.02)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    ax.contour(X, Y, Z)


def plot3d(ax):
    X = np.arange(-10, 10, 0.02)
    Y = np.arange(-10, 10, 0.02)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    ax.set_zlim(-11, 11)
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                    linewidth=0.01, antialiased=True, alpha=0.3)


class Gradient:
    def __init__(self, initial_x, initial_y, learning_rate, num_iterations):
        self.initial_x = initial_x

        self.initial_y = initial_y
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations

        self.fig1, self.ax1 = plt.subplots(figsize=(10, 10))  # 2d

        self.fig2 = plt.figure(figsize=(10, 10))  # 3d
        self.ax2 = self.fig2.gca(projection='3d')

        plot2d(self.ax1)
        plot3d(self.ax2)

    def step(self, x_current, y_current):
        x_gradient = 2 * x_current

        y_gradient = -2 * y_current

        new_x = x_current - x_gradient * self.learning_rate
        new_y = y_current - y_gradient * self.learning_rate

        self.ax1.arrow(x_current, y_current, - (self.learning_rate * x_gradient), - (self.learning_rate * y_gradient),
                   head_width=0.05, head_length=0.5, ec='red')
        self.ax2.quiver(x_current, y_current, (f(x_current, y_current)), - (self.learning_rate * x_gradient),
                    - (self.learning_rate * y_gradient), (-(f(x_current, y_current) - f(new_x, new_y))))

        return new_x, new_y

    def run(self):

        x = self.initial_x
        y = self.initial_y
        for i in range(self.num_iterations):
           x, y = self.step(x, y)

        return [x, y]


def start_from_point(x, y):
    print(f'Starting point ({x},{y})')
    gradient = Gradient(x, y, 0.08, 2000)
    x, y = gradient.run()
    print(f'Result f({x},{y}) = {f(x, y)}')
    plt.show()


start_from_point(5, 1)  # do -inf ?

start_from_point(5, 0)  # zbliza sie do punktu siodlowego