"""
#Modulos Padrao do pyhton:
#Modulos sao arquivos .py (Que contem codigo Python) e servem para expandir
#as funcionalidades padrao da linguagem.
#Veja todos os modulos padrao em Python em:
https://docs.python.org/3/py-modindex.html
"""
#importa tudo do sys
#import sys
from sys import platform           #importa apenas a funcao plarform
from sys import platform as os     #importa apenas a funcao plarform porem muda o nome para os
import random

while(True):
    numero = random.randint(0,100)
    print(numero)
    if numero == 1:
        break


print(numero)

