"""
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre
X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se
for o caso.
"""

x = int(input())
y = int(input())

maior = max(x , y)
menor = min(x , y)
soma = 0

for i in range(menor, maior+1):
    if i % 13 == 0:
        continue
    else:
        soma += i

print(soma)