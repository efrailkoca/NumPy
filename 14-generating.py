import numpy as np

a = np.zeros((2,3))         # sıfır matrisi yapar.
print(a)

b = np.ones((2,3))          # bir matrisi yapar.
print(b)                    
print(b.dtype)              # kendisi veri tipini float olarak belirler.

c = np.full((2,3), 5.0)     # sıfır ve bir haricinde bir şey yaptırmak için. 
print(c)

d = np.eye(3)               # köşegen matris oluşturmak için.
print(d)

e = np.arange(20)           # 0 dan 20 ye kadar(20 hariç) yapar.
print(e)

f = np.linspace(0,10,5)     # # 0 ile başlar, 10 a kadar gider, 5 tane sayı olacak şekilde.
print(f)                    