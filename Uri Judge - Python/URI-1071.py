"""Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos
na entrada que deverá caber em um inteiro."""

x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor += 1
soma = 0

while (menor < maior):
	if (menor % 2 != 0):
		soma += menor

	menor += 1
print(soma)
