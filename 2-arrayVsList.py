import numpy
l = [1,2,3]
a = numpy.array([1,2,3])

l.append(4)
print(l)
# a.append(4)   numpy bu özelliğe sahip değil.
print(a)

l = l + [5]
print(l)
a = a + numpy.array([4])    # bu yönteme "broadcasting" deniliyor.   # her sayıya eklediğimiz sayıyı ekler.
print(a)

l = l * 2       # aynı listeyi tekrar yazdırır.
print(l)
a = a * 2       # diziyi ikiyle çarpar.
print(a)

# a = numpy.sqrt(a)
# print(a)

a = numpy.log(a)
print(a)