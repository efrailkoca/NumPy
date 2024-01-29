import numpy as np

a = np.array([[1,2,6], [3,4,5], [7,8,9]])    # matris biçimine geldi
print(a)
print(a.shape)      # birinci sayı satır sayısını, ikinci sayı sütun sayısını verir.
print(a[0,1])       # matris içindeki bir sayıya ulaşmanın yolu.
print(a[:,0])       # sıfır sütununu gösterir.
print(a[0,:])       # sıfır satırını gösterir.
print(a.T)          # transpozu gösterir.
print(np.linalg.inv(a))     # tersini (inverse) hesaplar. matris kare olmalı.
print(np.linalg.det(a))     # determinantını hesaplar.
print(np.diag(a))           # köşegenleri yazdırır.
c = np.diag(a)
print(np.diag(c))           # bu şekilde de köşegen matris oluşturulur.