"""
Operador ternario
"""

logged_user = False

#Assim
msg = "Usuario logado." if logged_user == True else "usuario precisa logar."
#OU
if logged_user == True:
    msg = "Usuario logado."
else:
    msg = "precisa logar"

print(msg)


##############################################################################
idade = input("Qual a sua idade: ")

if not idade.isnumeric():
    print("Voce precisa digitar apenas numeros")
else:
    idade = int(idade)

    # Assim
    eh_de_maior = (idade >= 18)
    msg = "Pode acessar" if eh_de_maior == True else "Nao pode acessar"
    # ou
    if idade >= 18:
        print("Pode acessar")
    else:
        print("Nao pode acessar")

    print(msg)