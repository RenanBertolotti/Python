"""
Split, Join, Enumerate
* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #list / iteraveis
"""

string = "O Brasil é o o o pais do futebol, o Brasil é penta."
lista = string.split(" ")  #recebe uma lista baseado pela variavel string, cada indice da lista é a palavra tirando o " "espaço
lista2 = string.split(",") #recebe uma lista baseado pela variavel string, cada indice da lista é a palavra tirando a ","virgula

print(lista)
print(lista2)

#for valor in lista:
#    print( f" A palavra '{valor}' apareceu {lista.count(valor)}x na frase")


#######################################################################################
"""palavra = ''
contagem = 0

for valor in lista:
    qtdVezes = lista.count(valor)

    if qtdVezes > contagem:
        contagem = qtdVezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra} ({contagem})x")"""


#########################################################################################
#for valor in lista2:
#    print(valor.strip().capitalize()) #strip() remove o espaço do inicio e do final da String
                                      #capitalize() deixa a 1 palavra em maiusculo


##########################################################################################
lista3 = string.split(" ") #recebe uma lista baseado pela variavel string, cada indice da lista é a palavra tirando o " "espaço
string2 = ",".join(lista3) #junta os indices da lista3 atraves da virgula

print(string2)


#########################################################################################
for indice, valor in enumerate(lista):  #recebe um indice e o valor"conteudo" da lista
    print(f"{indice} , {valor}")

#OU fazer:

for indice in range(len(lista)):  #recebe um indice e o valor"conteudo" da lista
    print(f"{indice} , {lista[indice]}")


############################################################################################
lista4 = [ [1,2] , [3,4] , [5,6]]  #Lista dentro de Llista
print(lista4[0][0])     #mostra o indice 0 da lista, apos isso, mostra o indice 0 da lista do indice 0

for valor in lista4:
    print(valor[0])