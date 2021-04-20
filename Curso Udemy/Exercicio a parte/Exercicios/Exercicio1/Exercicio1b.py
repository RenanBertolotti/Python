"""Um engenheiro fez um sistema para controlar o acesso a uma sala confidencial. Para isso foi
determinado uma senha numérica com 4 algarismos, onde para ser válida todos seus números devem ser
diferentes de zero. Dessa forma, faça o algoritmo que colete um valor inteiro (senha numérica) e informe
se é uma senha “válida” ou inválida”. Dicas: utilize os operadores mod e div.
"""

senha = int(input("Digite sua senha numérica: "))

a = int(senha/1000)
b = int(senha%1000/100)
c = int(senha%100/10)
d = int(senha%10)

if (a==0) or (b==0) or (c==0) or (d==0):
    print("Invalido")
else:
    print("Valido")