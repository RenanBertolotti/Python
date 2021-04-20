nome = "Renan Bertolotti"
idade = 22
altura = 1.75
e_maior = idade > 18
peso = 58
imc = peso / (altura*altura)

print(nome)
print(idade)
print(altura)
print(e_maior)
print(peso)

print("Nome:", nome, ",idade: ",idade, ",altura: ",altura, ",Maior de idade:", e_maior, "peso:", peso)
print(idade*altura)

############    IMC   ###############
print("Nome:", nome, "tem", idade, "e seu IMC é:", imc)

idade1 = """10"""
print(idade1, type(idade1))