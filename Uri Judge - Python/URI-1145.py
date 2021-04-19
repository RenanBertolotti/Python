"""Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima
 linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo
abaixo. Não deve haver espaço em branco após o último valor da linha."""

digitados = input().split(" ")

x = int(digitados[0])
y = int(digitados[1])

valor = 1

while valor < y:
    for i in range(x):

        if i == x-1:
            print(valor, end="")
        else:
            print(valor, end=" ")

        valor += 1

    print()




