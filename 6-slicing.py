import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)

b = a[0,1:3]
print(b)
c = a[:,1]      # sütun için.
print(c)
d = a[-1,-2]    # tersten yazdırmak için.
print(d)