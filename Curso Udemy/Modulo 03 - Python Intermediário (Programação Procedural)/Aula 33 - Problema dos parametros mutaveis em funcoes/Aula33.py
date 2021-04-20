#Mutavel = Listas, dicionarios
#Imutavel = Tupla, String, Numero, Bool
"""
#EXEMPLO DE COMO NÂO FAZER UMA FUNCAO!!!!
def listadeclientes(lista_iteravel, novalista=[]):      #Exemplo de como noa fazer uma funcao
    novalista.extend(lista_iteravel)                    #pois passando uma nova lista como vazia, a funcao sempre adicionar
    return novalista                                    #as listas que sao envidas como parametro


clientes1 = listadeclientes(["Renan", "Maria", "Jose"])     #A lista CLIENTES1 vai conter a sua lista + a lista CLIENTES2
clientes2 = listadeclientes(["Ana", "Eduardo", "Gabriel"])  #A lista CLIENTES2 vai conter a sua lista + a lista CLIENTES1

print(clientes1)      #Print comprovando o erro
print(clientes2)      #Print comprovando o erro

#Para que isso nao aconteça é preciso fazer o seguinte
"""
#EXEMPLO DE COMO FAZER A FUNCAO!!!!
def listadeclientes(lista_iteravel, novalista=None):    #A novalista precisa ter como valor None
    if novalista is None:                               #Ele checa se a NovaLista é Nula(None) se for, a Novalista é vazia
        novalista = []
    novalista.extend(lista_iteravel)                    #fazendo isso, a NOVALISTA vai receber a lista_iteravel + a outra lista
    return novalista

listadeclientes1 = ["TESTE"]
clientes1 = listadeclientes(["Renan", "Maria", "Jose"], listadeclientes1 )   #A lista CLIENTES1 vai conter a sua lista + a lista CLIENTES2
clientes2 = listadeclientes(["Ana", "Eduardo", "Gabriel"])                   #A lista CLIENTES2 vai conter a sua lista + a lista CLIENTES1

print(clientes1)
print(clientes2)