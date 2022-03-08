import numpy as np
import itertools
A = np.random.randint(0,10, size = (100,10))
print(tuple(map(lambda a: np.linalg.norm(a), itertools.combinations(A, 2))))