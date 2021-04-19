"""Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores
nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos."""

list_num = []
soma = 0

for i in range(6):
    list_num.append(float(input()))

for i in list_num:
    if i > 0:
        soma += 1

print(f"{soma} valores positivos")