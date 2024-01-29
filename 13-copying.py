import numpy as np

a = np.array([1,2,3])
b = a
b[0] = 42
print(b)    # birinde değiştirirsek diğerinde de değişir.
print(a)

c = np.array([1,2,3])
d = c.copy()
d[0] = 42
print(c)
print(d)