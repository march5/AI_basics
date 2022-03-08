# Za pomocą biblioteki numpy przenumeruj wektor  , tzn zamień wartości  i  na  i .
# Przeskaluj macierz  , tak żeby wartości w każdej kolumnie mieściły się w zakresie [0, 1]
import numpy as np
from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
print(X.shape)
print(y.shape)

# print(y)
y = np.where(y == 0, -1, +1)  # if value == 0 we change it to -1, else to +1

# print(y)

for i in range(0, X.shape[1]):  # For every column we calculate its min and max
    Xmin = np.min(X[:, i])
    Xmax = np.max(X[:, i])
    X[:, i] = (X[:, i] - Xmin) / (Xmax - Xmin)  # then we change each value using the formula

print(X)
