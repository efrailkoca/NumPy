import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum())      # tüm sayıları toplar. sum() parantezinin içine bir şey yazmaz isek None algılar.
print(a.sum(axis=0))    # ayrı ayrı sütunları toplar.
print(a.sum(axis=1))    # ayrı ayrı satırları toplar.

print(a.mean(axis=1))   # satırların ortalamasını hesaplar.
print(a.mean(axis=0))   # her bir sütun için ortalamayı hesaplar.
print(a.mean())         # tüm sayıların ortalamasını hesaplar.

print(a.var())          
print(a.std())                  # bu ikisi aynı şey.
print(np.std(a, axis=None))     # bu ikisi aynı şey.

print(a.min(axis=None))         # min değer
print(np.max(a, axis=None))     # max değer