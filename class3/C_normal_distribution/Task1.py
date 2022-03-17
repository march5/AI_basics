import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
from matplotlib import cm

n1 = [0, 0]
cov1 = [[1, 0], [0, 1]]
cov2 = [[2, 0], [0, 1]]
cov3 = [[1, 0], [0, 2]]


x1, y1 = np.random.multivariate_normal(n1, cov1, 100).T
x2, y2 = np.random.multivariate_normal(n1, cov2, 100).T
x3, y3 = np.random.multivariate_normal(n1, cov3, 100).T

print(x3)


# plt.plot(X, Y, 'o')
Axes3D.plot_surface()

plt.show()

