from Aula26 import produtos, pessoas, lista
from functools import reduce


somaLista = reduce(lambda soma, i: soma+i, lista,0)
somaLista = reduce(lambda soma, p: soma+p['preco'], produtos,0)

print(somaLista)