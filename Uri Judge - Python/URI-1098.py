"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
"""

i = 0
j = 1

while i <= 2:
	for k in range(1, 4):

		if i == 0.0 or i == 1.0 or i == 2.0 or j == 1.0 or j == 2.0 or j == 3.0 or j == 4.0 or j == 5.0:
			print(f"I={i:.0f} J={j:.0f}")
		else:
			print(f"I={i:.1f} J={j:.1f}")

		j += 1

	i += 0.2
	j = 1 + i

