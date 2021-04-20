class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__conta = []

    @property
    def nome(self):
        return self.__nome

    @property
    def conta(self):
        self.listaContas()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @conta.setter
    def conta(self, conta):
        self.__conta.append(conta)

    def listaContas(self):
        for i in self.__conta:
            print(i)