"""Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
 uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado."""

num1, num2, num3 = input().split(" ")
num1, num2, num3 = int(num1), int(num2), int(num3)

listadigitada = [num1, num2, num3]

listdec = [num1, num2, num3]
listdec.sort()

for i in listdec:
    print(i)

print()

for i in listadigitada:
    print(i)
