from Aula24 import produtos, pessoas, lista

novalista = map(lambda x: x *2, lista)
novalista = list(novalista)

#print(novalista)


###################Maneiras de fazer uma lista com junçao de dicionario######################
def aumenta_preco(dicinario):
    dicinario['preco'] = dicinario['preco']*1.5
    return dicinario


def mudanome(dicionario):
    dicionario['nome'] = dicionario['nome']*2
    return dicionario


#ASSIm
precos = map(aumenta_preco,produtos)
nome = map(mudanome,produtos)
#ou assim
precos = map(lambda p: p['preco'],produtos)
nome = map(lambda  n: n["nome"],produtos)


print(list(precos))
print(list(nome))
