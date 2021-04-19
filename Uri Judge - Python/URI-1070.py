"""Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha,
inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares."""

numero = int(input())

contador = 6

for i in range(numero, (numero + 10000)):

    if contador == 0:
        break

    if not i % 2 == 0:
        print(i)
        contador -= 1