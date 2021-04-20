"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num1 = input("Digite um numero inteiro: ")

if not num1.isnumeric():
    print("ERRO: nao foi digitado numero")
else:
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f"O Numero {num1}, é par ")
    else:
        print(f"O Numero {num1}, é impar ")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite a hora: ")

if not hora.isnumeric():
    print("ERRO: nao foi digitado numero")
else:
    hora = int(hora)
    if hora>=0 and hora<=11:
        print("Bom dia")
    elif hora>=12 and hora<=17:
        print("Boa tarde")
    elif hora>=18 and hora<=23:
        print("Boa noite")
    else:
        print("Digite um horario valido")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite o seu nome: ")

if nome.isnumeric():
    print("Digite String")
else:
    if len(nome)<=4:
        print("Seu nome é curto")
    elif len(nome)>=5 and len(nome)<=6:
        print("Seu nome é normal")
    elif len(nome)>6:
        print("Seu nome é muito grande")
    else:
        print("digite um nome valido")