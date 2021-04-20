from abc import ABC,abstractclassmethod


class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @saldo.setter
    def saldo(self, saldo):
        if isinstance(saldo, (int,float)):
            self._saldo = saldo
        else:
            raise ValueError("Erro, o saldo precisa ser INT ou FLOAT")

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numerico")
        else:
            print("Deposito efetuado com sucesso.")
            self._saldo += valor
            self.detalhes()

    @abstractclassmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f"Agencia:{self._agencia}, Conta:{self._agencia}, Saldo:{self._saldo}")