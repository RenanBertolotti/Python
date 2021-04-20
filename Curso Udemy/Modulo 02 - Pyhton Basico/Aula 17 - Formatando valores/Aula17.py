"""
Formatando valores com modificadores

:s - Texto (Strings)
:d - Inteiros (Int)
:f - numeros de ponto flutuantes (float)
:. (NUMERO)f - Quantidade de casas decimais (float)  :.2f
: (Caractere) (> ou < ou ^) (Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ = Centro
"""

num1 = 5
num2 = 3
divisao = num1/num2
print(divisao)                      # 1.6666666666666667
print(f"{divisao}")                 # 1.6666666666666667
print(f"{divisao:.2f}")             # 1.67
print("{}".format(divisao))         # 1.6666666666666667
print("{:.2f}".format(divisao))     # 1.67
print(f"{num1:0>10}")               # 0000000005
print(f"{num1:0<10}")               # 5000000000
print(f"{num1:0^10}")               # 0000500000
print(f"{num1:0^10.2f}")            # 0005.00000


nome = "Renan bertolotti"
nomeFormatado = "{:@<50}".format(nome)
print(f"{nome:s}")                  # Renan bertolotti
print(f"{nome:#^50}")               # ################Renan bertolotti#################
print(nomeFormatado)                # Renan bertolotti@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


nome2 = "Renan Bertolotti"
nome2 = nome2.ljust(20, "#")        # Renan Bertolotti####
print(nome2)


