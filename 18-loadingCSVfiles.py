import numpy as np

# np.loadtxt, np.genfromtxt         =>         ikisi de aynı işe yarıyor. ikinci birazcık daha iyi olabilir.
# çünkü parametrelerimiz için daha fazla seçenek sunuyor.

data = np.loadtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data.shape)

data = np.genfromtxt ('spambase.csv', delimiter=",", dtype=np.float32)
print(data.shape)