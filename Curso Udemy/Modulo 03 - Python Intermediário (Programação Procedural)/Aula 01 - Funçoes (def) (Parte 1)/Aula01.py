"""
Funçoes - def
"""
def funcao():
    print("ola")


funcao()

###############################################
def funcaoParametro(msg):
    print(msg)


msg = "oi"
funcaoParametro(msg)
#OU
funcaoParametro("mesagem") #ele meio que cria uma mariavel para o argumento

###############################################
#def saudacao(msg="Mesagem", nome="Renan"): #Caso use paramentro com atribuição, vc pode chamar a funçar sem expecificar
def saudacao(msg, nome):                    #os argumentos, porem, ele vai receber os valores atribuidos!
    nome = nome.replace("e", "3")             #trata o nome, trocando "e" por 3
    print(msg, nome)


saudacao("Renan", "teste")                 #Enviando os argumentos
#saudacao()                               #Sem enviar os argumentos, ira receber os valores padrao ja expecificados
#saudacao(nome="Renan")                   #Envia apenas um valor de argumento, o outro argumento fica setado como padrao
#saudacao(nome="Renan",msg="Ola")         #Envia os 2 valores e nao precisa estar na ordem dos paramentros!

###################################################
def retonaAlgo(msg, nome):          #funcao que retorna algo recebendo parametros
    nome = nome.replace('e', "3")
    return f"{msg} {nome}"          #retorna o print com as variaveis

#Pode usar
msg = retonaAlgo("Ola", "Renan")
print(msg)
#ou
print(retonaAlgo("ola","renan"))



