"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print("Abrindo arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("Entrou na clase")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando arquivo")
        self.arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True #Tratei a exceçao


with Arquivo("abc.txt", "w") as arquivo:
    arquivo.write('alguma coisa')

#with open("abc.txt", "w") as arquivo:
#    arquivo.write('alguma coisa')
"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print("abrindo arquivo")
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()


with abrir("abc.txt", "w") as arquivo:
    arquivo.write("Ola mundo\n")
    arquivo.write("Ola mundo")

