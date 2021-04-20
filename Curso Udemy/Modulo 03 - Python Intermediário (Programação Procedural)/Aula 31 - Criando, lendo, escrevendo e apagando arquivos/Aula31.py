# https://docs.python.org/3/library/functions.html#open

"""
#Abrindo arquivos do jeito Pytonico: usando o "w+",
#"w+" serve para criar o arquivo(caso ja exista, ele apaga o antigo e cria um novo), tambem pode ler e escrever.
with open("abc.txt", "w+") as file:
    file.write("linha 1\n")
    file.write("linha 2\n")
    file.write("linha 3\n")

    file.seek(0,0)
    print(file.read())
    #Nao precisa fechar o arquivo, com o witch ele fecha sozinho!!

##################################################################################################################
#Abrindo arquivos do jeito Pytonico: usando o "r",
#"r" serve apenas para ler o arquivo!!
with open("abc.txt", "r") as file:
    file.seek(0,0)
    print(file.read())
    #Nao precisa fechar o arquivo, com o witch ele fecha sozinho!!

##################################################################################################################
#Abrindo arquivos do jeito Pytonico: usando o "a+",
#"a+" ativa o apendice mode, apenas adicionar no arquivo sem apagar ele, tambem pode ler!
with open("abc.txt", "a+") as file:
    file.write("Nova Linha\n")

    file.seek(0)
    print(file.read())
    #Nao precisa fechar o arquivo, com o witch ele fecha sozinho!!


##################################################################################################################
#Apagando arquivo!
import os
os.remove("abc.txt")  #apaga o arquivo criado

"""

##################################################################################################################
#UTILIZANDO JSON EM PYTHON
import json

d1 = {
    "Pessoa1":{
    "nome"  : "Luiz",
    "idade" : 55,
    },
    "Pessoa2": {
        "nome": "Renan",
        "idade": 22,
    },
}

d1_json = json.dumps(d1, indent=True)       #Converte o dicionario para o JSon

with open("abc.json","w+") as file:
    file.write(d1_json)
    file.seek(0,0)
    print(file.read())

print(d1_json)


##################################################################################################################
#Abrindo arquivo com "w+",baseado em outras linguagens!!
file = open("abc.txt", "w+")

file.write("Linha 1\n")
file.write("Linha 2\n")
file.write("Linha 3\n")

file.seek(0, 0)         #Server para resetar a leitura do arquivo, voltando pro começo
print("Lendo Linhas:")
print(file.read())      #Le todas as linhas!!!
print("#"*10)

file.seek(0,0)
print(file.readline(), end="") #Le apenas uma linha!  *obs:funcao end="" serve para nao pular linha automatico
print(file.readline(), end="") #Le apenas uma linha!  *obs:funcao end="" serve para nao pular linha automatico
print(file.readline(), end="") #Le apenas uma linha!  *obs:funcao end="" serve para nao pular linha automatico


file.seek(0,0)
print(file.readlines())       #mostra as imagen como lista, pode se utilizar o for!

#ASSIM
file.seek(0,0)
for i in file.readlines():
    print(i, end="")
#OU
file.seek(0,0)
for i in file:
    print(i, end="")

file.close()



##################################################################################################################
#Abrindo arquivos com Try: baseado em outras linguagens.
try:
    file = open("abc.txt","w+")
    file.write("Linha 1\n")
    file.write("Linha 2\n")
    file.write("Linha 3\n")

    file.seek(0,0)
    print(file.read(), end="")
except:
    print("erro ao ler o arquivo")
finally:
    file.close()

