"""
Zip - Unindo iteraveis
Zip Longest - Itertools
"""

###Codigo
cidades = ["Sao Paulo", "RIo de Janeiro", "Bahia", "Salvador"]
estados = ["SP", "RJ", "Ba"]

cidades_estado = zip(cidades, estados)  #O zip vai unir ate o menor indice, no caso ele remove o "SALVADOR"

for valor in cidades_estado:
    print(valor)


#pode converter para list e dicionario
cidades_estado = list(cidades_estado)
cidades_estado = dict(cidades_estado)


###################################################################
from itertools import zip_longest

cidades_estado = zip_longest(cidades, estados) #O zipLongest vai unir todos os indices, no caso ele coloca None para
                                               #quando nao tem mais indice
cidades_estado = zip_longest(cidades, estados, fillvalue="Estado") #O zipLongest vai unir todos os indices,o fillValue
                                                                #serve para deixar a string em vez de None

for valor in cidades_estado:
    print(valor)


##################################################################
from itertools import zip_longest, count

indice = count()
cidades = ["Sao Paulo", "RIo de Janeiro", "Bahia", "Salvador"]
estados = ["SP", "RJ", "Ba"]

cidades_estado = zip(indice, cidades , estados)

for i,c,e in cidades_estado:
    print(i, c, e)
