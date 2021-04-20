import numpy as np

def cria_tabuleiro():
	tabuleiro = np.zeros([8, 8], dtype=str)

	for i in range(8):
		for j in range(8):
			tabuleiro[i][j] = "_"

	return tabuleiro


def marca_tabuleiro(linha, coluna, tabuleiro):
	for i in range(8):
		for j in range(8):
			if linha == i and coluna == j:
				tabuleiro[i][j] = 'C'


def converte_coluna_numero(letra):
	lista_coluna = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

	if letra in lista_coluna:
		return lista_coluna.index(letra)
	else:
		return print("Letra invalida")


def percorre_direita_cima(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha - 1 >= 0 and coluna + 2 <= 7:
			if tabuleiro[linha - 1][coluna + 2] == '_':

				cavalo_linha -= 1
				cavalo_coluna += 2
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_direita_baixo(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha + 1 <= 7 and coluna + 2 <= 7:
			if tabuleiro[linha + 1][coluna + 2] == '_':

				cavalo_linha += 1
				cavalo_coluna += 2
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_baixo_direita(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha + 2 <= 7 and coluna + 1 <= 7:
			if tabuleiro[linha + 2][coluna + 1] == '_':

				cavalo_linha += 2
				cavalo_coluna += 1
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_baixo_esquerda(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha + 2 <= 7 and coluna - 1 >= 0:
			if tabuleiro[linha + 2][coluna - 1] == '_':

				cavalo_linha += 2
				cavalo_coluna -= 1
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_esquerda_baixo(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha + 1 >= 0 and coluna - 2 >= 0:
			if tabuleiro[linha + 1][coluna - 2] == '_':

				cavalo_linha += 1
				cavalo_coluna -= 2
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_esquerda_cima(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha - 1 >= 0 and coluna - 2 >= 0:
			if tabuleiro[linha - 1][coluna - 2] == '_':

				cavalo_linha -= 1
				cavalo_coluna -= 2
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


def percorre_cima_esquerda(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha - 2 >= 0 and coluna - 1 >= 0:
			if tabuleiro[linha - 2][coluna - 1] == '_':

				cavalo_linha -= 2
				cavalo_coluna -= 1
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)
		return
	except Exception as e:
		return


def percorre_cima_direita(linha, coluna, tabuleiro):
	global cavalo_linha
	global cavalo_coluna

	try:
		if linha - 2 >= 0 and coluna + 1 >= 0:
			if tabuleiro[linha - 2][coluna + 1] == '_':
				cavalo_linha -= 2
				cavalo_coluna += 1
				marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

		return
	except Exception as e:
		return


# -------------------------------------------------------#
tabuleiro = cria_tabuleiro()

cavalo_inicial = input("Digite o começo do cavalo: ")
cavalo_coluna = converte_coluna_numero(cavalo_inicial[0])
cavalo_linha = int(cavalo_inicial[1])

marca_tabuleiro(cavalo_linha, cavalo_coluna, tabuleiro)

for i in range(10000):
	percorre_cima_direita(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_direita_cima(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_direita_baixo(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_baixo_direita(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_baixo_esquerda(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_esquerda_baixo(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_esquerda_cima(cavalo_linha, cavalo_coluna, tabuleiro)
	percorre_cima_esquerda(cavalo_linha, cavalo_coluna, tabuleiro)


print(cavalo_linha, cavalo_coluna)
print(tabuleiro)
