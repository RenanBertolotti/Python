"""Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os
experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram
utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações,
ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de
cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso
de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere
Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em
relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto."""

casos_teste = int(input())
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(casos_teste):
	digitado = input().split(" ")

	numero = int(digitado[0])
	tipo = digitado[1]

	if tipo == "C":
		total_coelhos += numero
	elif tipo == "S":
		total_sapos += numero
	else:
		total_ratos += numero

total = total_ratos + total_sapos + total_coelhos
percentual_coelhos = (total_coelhos * 100) / total
percentual_ratos = (total_ratos * 100) / total
percentual_sapos = (total_sapos * 100) / total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
