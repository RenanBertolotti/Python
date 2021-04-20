"""

def falaoi():
    print("OI")


variavel = falaoi  #Voce pode atribuir uma variavel como uma funçao
variavel()         #variavel() se torna a funcao falaoi() !!!

#################################################################################

def master():                   #VOce pode criar uma funcao que escreva dentro dela uma outra funcao
    def slave():                #mas para que isso funcione, no final da funcao master, precisa chamar a funcao criada,
        print("Ola mundo")      #Ou retornar a funcao
    slave() #Assim ou
    #return slave #Assim


master()

###################################################################################

def master(funcao):             #VOce pode criar uma funcao que receba como parametro outra funcao!!!
    def slave():                #mas para que isso funcione, voce precisa chamar a funcao do parametro dento da funcao
        fala()
    slave() #Assim ou
    #return slave #Assim

def fala():
    print("fala")


master(fala)

###################################################################################

def master(funcao):                 #VOce pode criar uma funcao que receba como parametro outra funcao!!!
    def slave(*args, **kwargs):     #mas para que isso funcione, voce precisa chamar a funcao do parametro dentRo da funcao
        print("faz algo")
        funcao(*args, **kwargs)
    return slave

@master                            #voce pode Decorar as suas funcoes, mas para isso, precisa utilizar o @master
def fala():                        #O @master serve para a funcao master receber outras funcoes sem chamar elas
    print("fala")


@master
def novoprint(msg):
    print(msg)


novoprint("ola mundo")
"""
###################################################################################

from time import time
from time import sleep              #importa o sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start = time()
        resultado = funcao(*args, **kwargs)
        end = time()
        tempo = (end - start) * 1000
        print(f"A funcao {funcao.__name__} levou {tempo:.2f}ms para executar.")
        return resultado
    return interna


@velocidade
def demora():
    for i in range(100):
        print(i)


demora()
