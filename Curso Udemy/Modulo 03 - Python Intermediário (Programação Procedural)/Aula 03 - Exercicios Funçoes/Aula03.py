# 1 - Crie uma funçao que exibe uma saudaçao com os parametros saudaçao e nome

def saudacao(msg, nome):
    print(msg, nome)


saudacao("Bem vindo", "Renan")

#2 - Crie uma função que recebe 3 numeros como paramentro e exiba a soma entre eles
def soma(n1, n2, n3):
    return n1 + n2 + n3


print(soma(10, 10, 10))

#3 - Crie uma funçao que receba 2 numeroas. O primeiro é um valor e o segundo um percentual(ex. 10%). Retorne(return)
#o valor do primeiro numero somado do aumento do percentual do mesmo
def exercicio3(valor, porcento):
    return valor + float((valor/100) * porcento )


print(exercicio3(50, 10))
print(exercicio3(100, 10))
print(exercicio3(10, 10))
print(exercicio3(15, 100))

#4 - Fizz buzz - Se o paramentro da funçao for divisivel por 2 , retorne fizz,
#se o paramentro da função for divisivel por 5, retorne buzz, se o parametro da função for divisivel por 5 e por 3,
#retorne FizzBuzz, caso contrario, retorne o numero enviado
def fizzbuzz(valor):
    if valor % 2 == 0:
        return "fizz"
    elif valor % 5 == 0 and valor % 3 == 0:
        return "FizzBuzz"
    elif valor % 5 == 0:
        return "buzz"
    else:
        return valor


print(fizzbuzz(7))




