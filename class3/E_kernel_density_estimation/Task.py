import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from sklearn import cluster, datasets

n_samples = 100

data, y = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)

min = np.min(data)
max = np.max(data)

domain = np.linspace(min - 1, max + 1, 1000)
X, Y = np.meshgrid(domain, domain)

kernel = st.gaussian_kde(data.T, bw_method=0.17)
pos = np.vstack([X.ravel(), Y.ravel()])

evaluated = kernel.evaluate(pos)
Z = np.reshape(evaluated, X.shape)

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(data[:, 0], data[:, 1])
ax.contour(X, Y, Z, cmap='viridis')
ax.set_xlim(min - 1, max + 1)
ax.set_ylim(min - 1, max + 1)
plt.show()