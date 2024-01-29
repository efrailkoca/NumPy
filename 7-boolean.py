import numpy as np

a = np.array([[1,2], [3,4], [5,6]])
print(a)

bool_idx = a>3
print(bool_idx)     # true-false değerlerini gösteriyor.
print(a[bool_idx])  # koşulu sağlayan değerleri yazdırıyor.
print(a[a>3])       # bool kullanmadan yapmanın yolu.

b = np.where(a>3, a, -1)        # koşul sağlanıyorsa a daki değerleri aynen yazar. eğer sağlanmıyorsa değerler yerine -1 yazar.
print(b)


# dizinin içindeki elemanları indis olarak kullanmak;

c = np.array([10,19,30,48,64,89])
print(c)
d = np.array([1,3,5])
print(c[d])


e = np.array([10,19,30,48,64,89])
print(e)
even = np.argwhere(e%2==0).flatten()
print(e[even])