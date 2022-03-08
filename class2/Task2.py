import numpy as np

A = np.random.multivariate_normal(mean=[0, 0], cov=[[1, 0], [0, 10]], size=(100, 5))

print(A)
