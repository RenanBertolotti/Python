"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham metodos iguas( de mesma --
assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parametros
"""

from abc import ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f"B está falando {msg}")


class C(A):
    def fala(self, msg):
        print(f"C está falando {msg}")


b = B()
c = C()

b.fala("Um assunto")
c.fala("Outro Assunto")