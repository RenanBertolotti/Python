"""Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que
indique se estes valores foram digitados em ordem crescente ou decrescente.

Entrada
A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao
ser fornecido valores iguais para X e Y.

Saída
Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário
imprima a mensagem “Decrescente”."""

while True:
	numeros_lidos = input().split(" ")

	x = int(numeros_lidos[0])
	y = int(numeros_lidos[1])

	if x == y:
		break
	else:
		if max(x, y) == x:
			print("Decrescente")
		else:
			print("Crescente")