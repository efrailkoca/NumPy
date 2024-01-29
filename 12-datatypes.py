import numpy as np

x = np.array([1,0,2.1 ])
print(x)
print(x.dtype)      # numpy otomatik olarak veri tipini belirler.

y = np.array([1.3,2.1], dtype=np.int32)     # bu şekilde veri tipini değiştirebiliriz.
print(y)
print(y.dtype)