import re


def sequencia(cnpj):
	cnpj = removeCaracteres(cnpj)
	sequencial = cnpj[0] * len(cnpj)

	if sequencial == cnpj:
		return True
	else:
		return False


def removeCaracteres(cnpj):
	return re.sub(r"[^0-9]", "", cnpj)


def reconverteStr(lista):
	lista = [str(i) for i in lista]
	novaLista = ""
	for i in lista:
		novaLista += i

	return novaLista


def converteInteiro(lista):
	lista = [int(i) for i in lista]
	return lista


def primeiraSoma(cnpj, lista):
	cnpj = list(cnpj)
	lista = list(lista)

	soma = sum([x * y for x, y in zip(cnpj, lista)])
	return soma


def primeiroDigito(soma):
	soma = 11 - (soma % 11)

	if soma > 9:
		return 0
	else:
		return soma


def segundaSoma(cnpj, lista):
	cnpj = list(cnpj)
	lista = list(lista)

	soma = sum([x * y for x, y in zip(cnpj, lista)])
	return soma


def segundoDigito(soma):
	soma = 11 - (soma % 11)

	if soma > 9:
		return 0
	else:
		return soma


def comparaCnpj(cnpj_original, cnpj_copia):
	if cnpj_copia == cnpj_original:
		return True
	else:
		return False
