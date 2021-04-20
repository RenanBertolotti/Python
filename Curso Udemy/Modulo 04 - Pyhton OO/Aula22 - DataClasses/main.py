"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass


# @dataclass(eq=False, repr=False, order=False) #retira os metodos magicos criados automaticamente.
@dataclass
class Pessoa:
    __nome: str
    sobrenome: str

    def __post__init(self):
        self.nome_completo = self.__nome + " " + self.sobrenome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa("Renan", "Bertolotti")
p2 = Pessoa("Ivan", "Bertolotti")

print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo())
print("-----------------")
print(p1 == p2)
