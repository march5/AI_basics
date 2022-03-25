import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy import optimize

N = 100000
u = stats.uniform()
data = u.rvs(size=N)
mu = 0
sigma = 1

t = np.arange(-2, 2, 0.05)
num_bins = 50
fig, ax = plt.subplots(1, 1)
ax.hist(data, density=True, histtype='stepfilled', alpha=0.5, label='histogram')
ax.legend(loc='best', frameon=False)
ax.plot(t, stats.norm.pdf(t, mu, sigma), 'k-', lw=2, label='a=-1, b=1')
ax.legend()
# plt.show()

mu = sum(data)/N
sigma = np.sqrt(sum((x-mu)**2 for x in data)/N)
#mu, sigma = stats.norm.fit(data)
print(mu)
print(sigma)
t = np.arange(-2, 2, 0.05)
num_bins = 50
fig, ax = plt.subplots(1, 1)
ax.hist(data, density=True, stacked=True, histtype='stepfilled', alpha=0.5, label='histogram')
ax.legend(loc='best', frameon=False)
ax.plot(t, stats.norm.pdf(t,mu, sigma), 'k-', lw=2, label='a=-1, b=1')
ax.legend()
# plt.show()

#task 4

# split normal distribution pdf


def Gpdf(x, mu, sigma):
    return 1/(sigma * (2*np.pi)**.5) *np.e ** (-(x-mu)**2/(2 * sigma**2))


def l(x):
    mu, sigma = x
    return np.sum(np.log(Gpdf(data, mu, np.abs(sigma))))

# print(l(data, 0, 1))
# print(l(data, 0, 2))
# print(l(data, 1, 1))
# print(l(data, 0.5, 0.2))

# task 7

def f(x):
    x1, x2 = x
    return (x1+1)**2+(x2)**2


x0 = np.asarray((0, 0))  # Initial guess.
res1 = optimize.fmin_cg(f, x0)
print(res1)

x0 = np.asarray((1,1)) # Initial guess.
res1 = optimize.fmin_cg(l, x0)
print(res1)

# task 9