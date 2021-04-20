from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo, cliente):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo
        self.__cliente = cliente

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def cliente(self):
        return self.__cliente.__str__()

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Não é possivel sacar mais que o saldo")
        else:
            self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def __str__(self):
        return f"{self.agencia}, {self.numero}, {self.saldo}, {self.cliente}"