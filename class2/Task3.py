# Wypełni 100-elementową tablicę liczbami losowymi naturalnymi z zakresu  i policz liczbę wystąpień tych liczb.
# Która z tych liczb najczęściej występuje w tak wygenerowanej tablicy?

import numpy as np

A = np.random.randint(5, 16, size=100)

print(A)
B = np.bincount(A)
print(B)
print()
print(np.argmax(B))
