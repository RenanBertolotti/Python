"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo."""

valor = 7

for i in range(1, 10, 2):

	for j in range(valor, (valor - 3), -1):
		print(f"I={i} J={j}")

	valor += 2