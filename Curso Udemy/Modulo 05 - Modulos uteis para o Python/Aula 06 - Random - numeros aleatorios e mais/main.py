import random
import string

#############################USANDO COM INTEIRO#########################################################################
#gera um numero inteiro de 0 a 100, o argumento serve pra voce selecionar qual numero voce quer que sorteie
inteiro = random.randint(0,100) #gera um numero entre 0 a 100

#inteiro = random.randint(10,20) #gera um entre de 10 a 20
########################################################################################################################


#############################USANDO COM LISTAS##########################################################################
flutuante = random.uniform(0,100) #gera um numero de ponto flutuante entre 0 a 100

#Gera um numero aleatorio que voce pode setar de qual a qual valor e ainda pode setar pular em valor,nesse exemplo:
#ele vai de 900 a 1000 e pula de 10 em 10
novo_inteiro = random.randrange(900,1000, 10)
novo_flutuante = random.random() #gera entre 0.0 a 0.9999999999999999
########################################################################################################################


#############################USANDO COM LISTAS##########################################################################
lista_sorteio = ["Renan","Ana","Maria","Rose","Janny","Danilo","Felipe"] #lista completa
resultado_sorteio = random.choice(lista_sorteio) #Gera um numero/indice aleatorio de uma lista!

#tambem existe o "choices", voce seta quantos numeros aleatorios da lista ele vai gerar, POREM PODE-SE REPETIR!!
resultado_sorteio_comChoices = random.choices(lista_sorteio, k=3) #Gera 2 numeros aleatorios da lista, porem pode-se repetir!!

#tambem existe o "sample", voce seta quantos numeros aleatorios da lista ele vai gerar, MAS NAO SE REPETE!!
resultado_sorteio_comSample = random.sample(lista_sorteio, k=3) #Gera 2 numeros aleatorios da lista,mas nao se repete

#Caso queira embaralhar uma lista ja criada, precisa utilizar o "shuffle"
random.shuffle(lista_sorteio) #A sua lista_sorteiro vai ficar embaralhada, nao é possivel criar uma variavel para receber essa lista!
########################################################################################################################



##################################GERAR SENHA ALEATORIA#################################################################
letras = string.ascii_letters       #a variavel "letra" vai receber todas as letras do alfabeto
digitos = string.digits             #a variavel "digitos" vai receber todas os digitos do teclado, ou seja, de 0 a 9
caracteres = "!@#$%¨&*()_+"         #seta a variavel "caracteres" para para receber os caracteres escolhidos
geral = letras+digitos+caracteres   #a variavel "geral" vai receber a junção das variavel anteriores

senha_gerada = "".join(random.choices(geral, k=20)) #gera a senha aleatoria ate 20 caracteres a partir da variavel "geral"
                                                    #ou seja, ele vai pegando um indice aleatorio da variavel "geral" e
                                                    #colocando em uma string
########################################################################################################################


print("Resultados Gerados: ")
print(inteiro)
print(flutuante)
print(novo_flutuante)
print(novo_inteiro)
print(resultado_sorteio)
print(resultado_sorteio_comChoices)
print(resultado_sorteio_comSample)

print("\n\n")
print("Senha Gerada: ")
print(senha_gerada)