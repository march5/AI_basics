import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

f = lambda x: np.exp(x)
x = np.linspace(0., 21, 200)
y = f(x)

plt.figure(figsize=(6,6))
axes = plt.gca()
axes.set_xlim([-1,21])
plt.plot(x, y, 'ok', ms=3)
plt.show()

corr = {}
corr['pearson'], _ = stats.pearsonr(x, y)
corr['spearman'], _ = stats.spearmanr(x, y)
corr['kendall'], _ = stats.kendalltau(x, y)
print(corr)
