"""Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo."""

lista_valores = []
maior = 0
indice = 0

for i in range(1,101):
	valor_digitado = int(input())

	lista_valores.append(valor_digitado)

	if valor_digitado > maior:
		maior = valor_digitado
		indice = i

print(f"{maior}")
print(f"{indice}")
