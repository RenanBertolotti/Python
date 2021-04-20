
variavel="Renan"        #esta no escopo global


def func():
    print(variavel)


def func2():                  #USAR O GLOBAL NAO E UMA BOA PRATICA DE PROGRAMAÇAO, O CERTO È ENVIAR COMO PARAMETRO OU USAR O RETURN
#   global variavel           #para poder Editar a variavel de dentro da funçao precisa utilizar o GLOBAL
    variavel = "Outro Valor"  #se editar a variavel dentro da funçao, ELA NAO MUDA O VALOR GLOBAL!!!
    print(variavel)


def func3(arg=None):                #Uso correto para tratar variaveis globais!!
    arg = arg.replace('n', "c")
    return arg


def func4():                #funçao da Erro, nao pode usar uma variavel global e mudar o valor dela depois de usar ela
    print(variavel)
    variavel = 1324
    print(variavel)


func()              #Renan
func2()             #Outro Valor
variavel = func3(variavel)  #muda o valor da "VARIAVEL"
print(variavel)     #Renan
func4()             #ERRO

######################################################################################################

