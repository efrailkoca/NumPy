import numpy as np

A = np.array([[1,1], [1.5, 4]])
b = np.array([2200, 5050])
x = np.linalg.inv(A).dot(b)         # inverse kullanmak birazcık yavaş olduğu asıl yol bu değil.
print(x)


x = np.linalg.solve(A, b)           # daha iyi yol.
print(x)