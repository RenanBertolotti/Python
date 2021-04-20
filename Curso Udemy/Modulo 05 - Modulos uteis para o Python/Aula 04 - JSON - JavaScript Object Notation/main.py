"""
JavaScript Object Notation - JSON
JSJON (JavaScript Object Notation) é um formato de troca de dados entre sistemas e programas muito leve e de fácil utilização.
Muito Utilizado por APIs

https://docs.python.org/3/library/json.html  == Documentação
"""

from dados import *
import json

#Para converter de python para json!!
#converte o dado json para a variavel criada
dados_json = json.dumps(clientes_dicionario)
#comando para identar o codigo para deixar mais legivel= dados_json = json.dumps(clientes_dicionario, indent=4)

print(type(dados_json))
print(dados_json)
#-------------------------------------------------------------------------------------------------#

#Para converter de json para Python!!
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)
#-------------------------------------------------------------------------------------------------#


##############################################################################################
#Salvar o Json em um arquivo
with open("clientes.json", 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

#Ler o Json dentro de um arquivo
with open("clientes.json", 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)







