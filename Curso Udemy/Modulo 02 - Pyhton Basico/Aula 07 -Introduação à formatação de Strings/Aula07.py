"""
Introdução a formatação de Strings
"""
nome = "Renan Bertolotti"
idade = 22
altura = 1.75
e_maior = idade > 18
peso = 58
imc = peso / (altura*altura)

print("Nome:", nome, "tem", idade, "e seu IMC é:", imc)
print(f"{nome}, imc:{imc:.2f}")
print("{}, imc:{:.2f}".format(nome, imc))
print("{0}, imc:{1}".format(nome, imc))
print("{n}, imc:{i}".format(n=nome, i=imc))

#################   DESAFIO     #####################
"""
* Criar variaveis para nome(str), idade(int);
* Altura (Float) e peso (Float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento
* Obter o imc com 2 casas decimais
* Exibir um texto com todos os valores
"""

nome = "Renan"
idade = 22
altura = 1.75
peso = 58.60
ano_atual = 2020
imc = peso / (altura*altura)
anoNascimento = ano_atual - idade

print("Nome:{} ,Idade:{} ,Altura:{}, Peso:{}, Ano Atual:{}, IMC:{:.2f}, Nasceu em:{}".format(nome, idade, altura, peso, ano_atual, imc, anoNascimento))
print(f"Nome:{nome} ,Idade:{idade} ,Altura:{altura}, Peso:{peso}, Ano Atual:{ano_atual}, IMC:{imc:.2f}, Nasceu em:{anoNascimento}")
