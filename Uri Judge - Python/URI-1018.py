"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode
ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de
notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem:
“Presentation Error”."""

valor = int(input())
temp = valor

nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0

if valor >= 100:
    nota100 = int(valor / 100)
    valor = int(valor % 100)

if valor >= 50:
    nota50 = int(valor / 50)
    valor = int(valor % 50)

if valor >= 20:
    nota20 = int(valor / 20)
    valor = int(valor % 20)

if valor >= 10:
    nota10 = int(valor / 10)
    valor = int(valor % 10)

if valor >= 5:
    nota5 = int(valor / 5)
    valor = int(valor % 5)

if valor >= 2:
    nota2 = int(valor / 2)
    valor = int(valor % 2)

if valor >= 1:
    nota1 = int(valor / 1)
    valor = int(valor % 1)

print(f"{temp}")
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
