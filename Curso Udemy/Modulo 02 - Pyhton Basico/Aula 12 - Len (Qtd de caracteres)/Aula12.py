
usuario = input("Digite seu usuário: ")
qtd_char = len(usuario)
print(usuario, qtd_char, type(qtd_char))

if qtd_char < 6:
    print("escreva uma senha com mais de 6 caracteres")
else:
    print("senha cadastrada com sucesso")

#################################################################################

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A qtd total foi: {len(string1+string2)}")
#OU
print(f"A qtd total foi: {len(string1)+len(string2)}")

print(string2.__len__())