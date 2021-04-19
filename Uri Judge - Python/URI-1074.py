"""Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido,
mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE)
ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL)
, pois por definição zero é par, seu programa deverá imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de
teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser
maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha."""

vezes_loop = int(input())

for i in range(vezes_loop):
	numero_lido = int(input())

	if numero_lido == 0:
		print("NULL")
		continue

	if numero_lido %2 == 0:
		print("EVEN", end=" ")
	else:
		print("ODD", end=" ")

	if numero_lido > 0:
		print("POSITIVE")
	elif numero_lido < 0:
		print("NEGATIVE")
