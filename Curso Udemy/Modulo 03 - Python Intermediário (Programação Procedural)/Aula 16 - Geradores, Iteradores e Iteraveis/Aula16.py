import sys
import time

lista = [0, 1, 2, 3, 4, 5]

lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, "__next__"))


#-----------------------------------------------------------
lista2 = list(range(1000))

print(sys.getsizeof(lista2))


#----------------------------------------------------------
def gera1():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)

    return r


def gera2():
    r = []
    for n in range(100):
        yield n                 #envia cada valor de uma vez
        time.sleep(0.1)


r = gera1()
for i in r:
    print(i)