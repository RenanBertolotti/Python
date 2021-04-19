"""Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de
3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3
valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com
três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo."""

numeros_casos = int(input())

for i in range(numeros_casos):
	numeros_lidos = input().split(" ")
	numeros_lidos = float(numeros_lidos[0]), float(numeros_lidos[1]), float(numeros_lidos[2])

	media_ponderada = ((numeros_lidos[0]*2) + (numeros_lidos[1]*3) + (numeros_lidos[2]*5)) / (2+ 3 + 5)
	print(f"{media_ponderada:.1f}")
