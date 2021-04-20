import math

PI = math.pi

def dobraLista(lista):
    return [x*2 for x in lista]


def multiLista(lista):
    return [x*x for x in lista]


def somaLista(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma


lista = [1, 2, 3, 4, 5]

#print(somaLista(lista))
#print(PI)
print(__name__)