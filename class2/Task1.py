# Policz odległość euklidesową pomiędzy kazdą parą 100 punktów w 10 wymiarowej przestrzeni
import numpy as np

A = np.random.randint(0, 10, size=(100, 10))


def eudist(x, row):
    return ((x - A[:])**2).sum(axis=1)


print(A)
print()
for i in range(0, 100):
    print(eudist(A[i], i))





