import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import scipy.stats as stats
from scipy.stats import multivariate_normal

cov_mean = X.mean(axis=0)
covariance_matrix = np.cov(X.T)

X3_rv = multivariate_normal(cov_mean, covariance_matrix)
X3 = X3_rv.rvs(1000)

# contours
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

H, P = np.meshgrid(x, y)

pos = np.empty(H.shape + (2,))
pos[:, :, 0] = H;
pos[:, :, 1] = P

# eigen values
eig = np.linalg.eig(covariance_matrix)
eigenvalues = eig[0] * 5
eigenvectors = eig[1]

# plot
origin_point = np.array([[0, 0], [0, 0]])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))

# sample
ax.scatter(X3[:, 0], X3[:, 1])

# contours
ax.contour(H, P, X3_rv.pdf(pos), levels=5, colors='red')

# eigenvectors
ax.quiver(*origin_point, eigenvectors[0], eigenvectors[1], scale=30)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
plt.show()