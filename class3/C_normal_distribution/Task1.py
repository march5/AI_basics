import matplotlib.pylab as plt
import numpy as np
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
from matplotlib import cm

# zad 1
mean = np.array([0,0])
cov = np.array([[1,0], [0,1]])
# mean = np.array([0,0])
# cov = np.array([[2,0], [0,1]])
# mean = np.array([0,0])
# cov = np.array([[1,0], [0,2]])
x = np.linspace(-3,3,500)
y = np.linspace(-3,3,500)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y
rv = stats.multivariate_normal(mean = mean, cov = cov)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
plt.show()

# zad 2
pos = np.array([X.flatten(),Y.flatten()]).T
fig = plt.figure(figsize=(5,5))
ax0 = fig.add_subplot(111)
ax0.contour(rv.pdf(pos).reshape(500, 500))

plt.show()
