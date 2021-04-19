"""Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero)
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos
entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai
conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo."""

while True:
	numeros_digitados = input().split(" ")

	m = int(numeros_digitados[0])
	n = int(numeros_digitados[1])

	if m < 1 or n < 1:
		break
	else:
		maior = max(m, n)
		menor = min(m, n)

		soma = 0

		for i in range(menor, maior+1):
			soma += i
			print(i, end=" ")

		print(f"Sum={soma}")
