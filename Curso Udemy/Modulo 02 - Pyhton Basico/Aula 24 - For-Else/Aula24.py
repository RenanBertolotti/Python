"""
For / Else
"""

variavel = ["Renan" , "Gabriel", "Maria"]


for valor in variavel:
    if valor.startswith("M"):
        print("Começa com M", valor)
    else:
        print("Não começa com M", valor)


###################################################################
comecaComJ = False

for valor in variavel:
    if valor.startswith("J"): # ou usar if valor.lower().startswith("j"):  == ele checa se é letra e maiuscula ou minuscula
        comecaComJ = True


if comecaComJ == True:
    print("existe uma palavra que comeca com M")
else:
    print("Nao existe uma palvra que começa com M")


###################################################################
comecaComJ = False

for valor in variavel:
    print(valor)
    if valor.startswith("G"): # ou usar if valor.lower().startswith("j"):  == ele checa se é letra e maiuscula ou minuscula
        continue
else:
    print("Nao existe uma palvra que começa com M")