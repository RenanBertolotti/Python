"""
Combinations , Permutations e Product - Itertools

Combinations - Ordem nao importa
Permutations - Ordem importa
Ambos não repetem valores unicos
Product - Ordem importa e repete valores unicos
"""
from itertools import combinations

pessoas = ["Renan", "Ana", "Maria", "Rose", "Leticia"]

for grupo in combinations(pessoas,2):
    print(grupo)

############################################################################
print("#"*1000)
############################################################################
from itertools import permutations


pessoas = ["Renan", "Ana", "Maria", "Rose", "Leticia"]

for grupo in permutations(pessoas,2):
    print(grupo)


############################################################################
print("#"*1000)
#############################################################################
from itertools import product


pessoas = ["Renan", "Ana", "Maria", "Rose", "Leticia"]

for grupo in product(pessoas, repeat=2):
    print(grupo)


