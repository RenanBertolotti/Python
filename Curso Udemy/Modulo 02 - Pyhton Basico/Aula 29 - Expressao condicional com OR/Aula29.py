
nome = input("Qual o seu nome?: ")

#Assim
print(nome or "Voce nao digitou nada")
#OU
if nome:  #checa se digitou algo
    print(nome)
else:
    print("Voce nao digitou nada")


###########################################################################
a = 0
b = None
c = False
d = []
e = {} #Dicionario
f = 22
g = "Renan"

variavel = a or b or c or d or e or f or g #recebe o primeiro valor que retorna VERDADEIRO, no caso seria a variavel F

print(variavel)