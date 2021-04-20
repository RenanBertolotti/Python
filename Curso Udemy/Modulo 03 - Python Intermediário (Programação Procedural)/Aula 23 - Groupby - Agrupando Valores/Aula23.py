"""
Groupby - Agrupando valores
"""
from itertools import groupby

alunos = [
    {"nome" : "Renan", "nota" : "A"},
    {"nome" : "Ana", "nota" : "B"},
    {"nome" : "Maria", "nota" : "C"},
    {"nome" : "Jean", "nota" : "D"},
    {"nome" : "Luiz", "nota" : "E"},
    {"nome" : "Andre", "nota" : "A"},
    {"nome" : "Anderson", "nota" : "B"},
    {"nome" : "Sueli", "nota" : "C"},
    {"nome" : "Jose", "nota" : "D"},
]
#ASSIm
alunos.sort(key=lambda intem: intem['nota'])
#ou
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for aluno, valores_agrupados in alunos_agrupados:
    print(aluno)

    #quantidade = len(list(valores_agrupados))      #Monstra a qtd de pessoas que tiraram X nota
    #print(quantidade, aluno)

    for i in valores_agrupados:
        print(i)


