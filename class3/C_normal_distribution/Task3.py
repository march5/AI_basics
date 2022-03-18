#zestaw C zad 3
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
from matplotlib import cm
#zad 3
n=[0,0]
cov1 = [[1,0],[0,1]]
cov2 = [[2,0],[0,1]]
cov3 = [[1,0],[0,2]]
X1_rv=stats.multivariate_normal(n, cov1)
X1 = X1_rv.rvs(1000)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.scatter(X1[:, 0], X1[:, 1])
ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
plt.show()
X2_rv=stats.multivariate_normal(n, cov2)
X2 = X2_rv.rvs(1000)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.scatter(X2[:, 0], X2[:, 1])
ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
plt.show()
X3_rv=stats.multivariate_normal(n, cov3)
X3 = X3_rv.rvs(1000)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.scatter(X3[:, 0], X3[:, 1])
ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
plt.show()
