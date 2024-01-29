import numpy as np

a = np.random.random((3,2))     # 0-1 arasında random sayı üretir. 
print(a)

b = np.random.randn()
print(b)

c = np.random.randn(1000)
print(c.mean(), c.var())

d = np.random.randint(3,10,size=(3,3))          # 3 ile 10 aralığında 3e3 matris olulturmak için.
print(d)

e = np.random.choice(5,size=10)                 # 0 ile 5 aralığında yazdırır.
print(e)

f = np.random.choice([-8,-7,-6],size=10)                 # 3 sayıdan birini seçer.
print(f)