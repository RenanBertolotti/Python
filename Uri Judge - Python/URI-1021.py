"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal."""

valor = float(input())

temp = valor
moeda = round(temp - int(temp), 2)
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = moeda1 = moeda05 = moeda025 = moeda010 = moeda005 = moeda001 = 0

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
    moeda1 = int(valor / 1)
    valor = int(valor % 1)

if moeda >= 0.50:
    moeda05 = int(moeda / 0.5)
    moeda = round((moeda % 0.5), 2)

if moeda >= 0.25:
    moeda025 = int(moeda / 0.25)
    moeda = round((moeda % 0.25), 2)

if moeda >= 0.10:
    moeda010 = int(moeda / 0.10)
    moeda = round((moeda % 0.10), 2)

if moeda >= 0.05:
    moeda005 = int(moeda / 0.05)
    moeda = round((moeda % 0.05), 2)

if moeda >= 0.01:
    moeda001 = int(moeda / 0.01)
    moeda = round((moeda % 0.01), 2)

print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda05} moeda(s) de R$ 0.50")
print(f"{moeda025} moeda(s) de R$ 0.25")
print(f"{moeda010} moeda(s) de R$ 0.10")
print(f"{moeda005} moeda(s) de R$ 0.05")
print(f"{moeda001} moeda(s) de R$ 0.01")
