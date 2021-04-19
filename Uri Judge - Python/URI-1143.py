"""
Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão
apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
"""

casos_teste = int(input())

valor = 1

for i in range (1, casos_teste+1):
    print(f"{i} {i**2} {i**3}")