"""
Tipos de dados
String - str  == Texto 'assim' ou "assim"
Inteiro - int == 1, 2, 3, 4, 5
Float - real/flutuante = 1.12313, 2.465456, 3.465465
Bool - Booleane/logico = true or false
"""

print("Luiz", type("Luiz"))
print(10, type(10))
print(10.5, type(10.5))
print(True, type(True))
print("Renan"=="Renan", type("Renan"=="Renan"))

print("Renan", type("Renan"), bool("Renan"))
print("10", type("10"), type(int("10")))

nome = "443.06347850"
print(nome, float(nome))

##############################################################
print("Renan", type("Renan"))
print(22, type(22))
print(1.75, type(1.75))
print(22 >= 18, type(22 >=18))