import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape(2,3)          # a'yı ikiye üç (2,3) matrisi haline getirir.
print(b)

c = a[np.newaxis, :]
print(c)
print(c.shape)

d = a[:, np.newaxis]
print(d)
print(d.shape)