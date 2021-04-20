"""
Desempacotamento de listas
"""

lista = ["Renan", "Edson", "Ivan"]

n1, n2, n3 = lista  # cada variavel vai recer um valor de cada indice , porem precisa declaras as variaveis de acordo com o indice da lista!!!
#n1, n2 = lista  # DA ERRRO!! nao pode ser variavel menor que o indice da lista, porem tem como arrumar igual a linha de baixo
n1, n2, *outra_lista = lista  # o * serve para gerar outra lista com o restante dos valores!!!
                              #exemplo:  lista = ["Renan", "Edson", "Ivan", 3, 2, 1]
                              #outralista == ["Ivan", 3, 2, 1]

print(outra_lista)

########################################################################################################
lista = ["Renan", "Edson", "Ivan", 3, 2, 1, 10]

n1, n2, *outra_lista, ultimoDaLista = lista # o *recebe tudo menos o ultimo e o n1 e n2

print(ultimoDaLista)