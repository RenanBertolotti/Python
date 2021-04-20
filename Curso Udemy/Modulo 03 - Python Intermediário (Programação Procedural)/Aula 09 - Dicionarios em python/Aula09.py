"""
Dicionario em Python
#Nas listas existe indices, ja no dicionario voce que controla o indice/chave
"""

#pode se criar assim:
d1 = dict(chave1= "valor da chave", chave2 = "Valor da outra chave" , chave3 = "ola mundo")
#ou assim
dicionario ={"chave1" : "valor"}
#ou assim
dicionario["nova_chave"] = "valor da nova chave"

#no dicionario nao se pode criar chaves iguais, elas precisam ser unicas

if "chave3" in d1:          #checa se existe a chave3 no dicionario
    print(d1["chave3"])
#OU
if d1.get("chave3") is not None:
    print(d1.get("chave3"))

#Alterando valor com dicionario,assim:
d1['chave1'] = "novoValor1"
#ou
d1.update({"chave1":"novoValor2"})

#Adicionando uma nova chave,assim:
d1.update({"chave4":"teste"})
#OU
d1["chave4"] = "teste"

#Removendo chaves/valores do dicionario:
del d1["chave4"]

print(dicionario)                   #imprime o dicionario inteiro
print(dicionario["chave1"])         #imprime o dicionario com a chave "chave1"
print(d1)

print(d1.keys())   #imprime apenas todas as chaves
print(d1.values()) #imprime apenas todos os valores
print(d1.items())  #imprime todos os itens do dicionario, separando-os
print(len(d1))     #imprime o tamanho total dos indices existentes no dicionario

#imprimindo os valores por FOR
for chave in d1:  #imprime apenas as chaves
    print(chave)

for valor in d1.values(): #imprime apenas os valores
    print(valor)

#Assim:
for item in d1.items(): #imprime todos os valores, chaves e valor
    print(item)
    print(item[0], item[1]) #imprime os valores separadamente
#OU
for chave,valor in d1.items():
    print(chave, valor)


######################DICIONARIO DENTRO DE DICIONARIO#################################
clientes = {
   "cliente1" : {
     "nome" : "Luiz",
     "sobrenome" : "otavio",
   },
   "cliente2" : {
     "nome" : "Renan",
     "sobrenome" : "Bertolotti",
   }
}

for clientes_k, clientes_v in clientes.items():
    print(f"Exibiindo {clientes_k}" )
    for dados_k, dados_v in clientes_v.items():
        print(f"\t {dados_k} = {dados_v}")


############################ O sinal de = passa apenas o ponteiro dele #####################################
d1 = {1:"a", 2:"b", 3:"c"}
v = d1                          # v é igual o d1, se mudar o v, muda o di

print(d1)
print(v)

###Para criar um novo dicionario como copia:
v = d1.copy()       #v é um novo dicionario, nao é mais o ponteiro do d1!!

v[1] = "Renan"     #agora ele consegue alterar apenas o v
print(v)


######################## CONVERTENDO VALORES PARA DICIONARIO #####################
lista = [ ["c1", 1], ["c2", 2], ["c3", 3] ]

d1 = dict(lista) #convertendo a lista para o dicionario
print(d1)

tupla = ( ("c1", 1), ("c2", 2), ("c3", 3) )
d1 = dict(tupla) #convertendo a tupla para o dicionario
print(d1)


########################## Removendo itens #######################################
d1.pop("c2")      #remove o item escolhido "c2"
d1.popitem()      #remove o ultimo item do dicionario
print(d1)
