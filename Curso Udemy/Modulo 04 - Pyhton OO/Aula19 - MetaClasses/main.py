"""
EM PYTHON TUDO E UM OBJETO: incluindo classes
Metaclasses são as 'classes' que criam classes.
Ex: type é uma metaclasse(!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if "b_fala" not in namespace:
            print(f"Oi, voce precisa criar o metodo b_fala em {name}")
        else:
            if not callable(namespace['b_fala']):
                print(f"O metodo b_fala precisa ser um metodo, nao um atributo na classe:{name}")

        if "attr_classe" in namespace:
            print(f"{name} tentou sobrescrever o atributo")
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = "Valor A"

    def b_fala(self):
        print("Classe A disse oi")


class B(A):
    attr_classe = "Valor B"

    def b_fala(self):
        print("Classe B disse oi")


class C(B):
    attr_classe = "Valor C"


a = A()
b = B()
c = C()
#         Nome, Herança, Atributos)
#           |    |       |||
# d = type("D",  (),    'attr' : "Ola Mundo") #Voce consegue criar classe usando o type.
# print(d.attr)

print(b.attr_classe)
print(c.attr_classe)
