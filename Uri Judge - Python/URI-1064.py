"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha,
deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números
será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores
positivos digitados."""

lista = []

for i in range(6):
    x = float(input())
    lista.append(x)

lista_positivo = []

for i in lista:
    if i > 0:
        lista_positivo.append(i)

media = sum(lista_positivo) / len(lista_positivo)

print(f"{len(lista_positivo):.0f} valores positivos")
print(f"{media:.1f}")
