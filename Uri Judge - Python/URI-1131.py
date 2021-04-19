"""A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de
vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após
escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser
executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser
encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine
empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio
respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado
devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa
sem acento, conforme o exemplo abaixo."""

jogos = 0
vitoria_inter = 0
vitoria_gremio = 0
empate = 0

while True:
	gols_digitado = input().split(" ")
	gols_inter = int(gols_digitado[0])
	gols_gremio = int(gols_digitado[1])

	jogos += 1

	if gols_inter > gols_gremio:
		vitoria_inter += 1
	elif gols_gremio > gols_inter:
		vitoria_gremio += 1
	else:
		empate += 1

	continua = int(input("Novo grenal (1-sim 2-nao)\n"))

	if continua == 2:
		break
	if continua == 1:
		continue

	while continua != 2 and continua != 1:
		continua = int(input("Novo grenal (1-sim 2-nao)\n"))

	if continua == 2:
		break

print(f"{jogos} grenais")
print(f"Inter:{vitoria_inter}")
print(f"Gremio:{vitoria_gremio}")
print(f"Empates:{empate}")

if vitoria_inter > vitoria_gremio:
	print("Inter venceu mais")
elif vitoria_inter < vitoria_gremio:
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")