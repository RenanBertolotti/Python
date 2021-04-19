"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na
execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
"""

casos_teste = int(input())

valor = 1

for i in range(casos_teste):
	for k in range(valor, valor + 3):
		print(k, end=" ")

	print("PUM")

	valor += 4
