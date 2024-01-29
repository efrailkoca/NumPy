import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b))                   # iki diziyi birleştirmek için.
print(c)
c = np.concatenate((a,b), axis=None)        # satır sayısını bu şekilde ayarlayabiliriz.
print(c)

d = np.concatenate((a,b.T), axis=1)
print(d)

# hstack : horizontally stack   -   vstack : vertically stack ;

e = np.array([1,2,3,4])
f = np.array([5,6,7,8])

# hstack;
g = np.hstack((e,f))
print(g)

# vstack;
h = np.vstack((e,f))
print(h)