# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        print("Eu sou o Init")

    def __call__(self, *args, **kwargs):
        resultado = 0

        for i in args:
            resultado += i

        return resultado

    def falaOi(self):
        print("oi")

    def __setattr__(self, key, value):
        if key == "nome":
            self.__dict__[key] = "VOce nao pode fazer isso"
        else:
            self.__dict__[key] = value

    def __del__(self):
        print("Objeto coletado")

    def __str__(self):
        return f"Nome da classe: {A.__name__}, valor: {self.nome}"

    def __len__(self):
        return 999


a = A()
print(a(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
a.falaOi()
a.nome = "Luiz Otavio"
print(a)
print(a.nome)
print(len(a))
