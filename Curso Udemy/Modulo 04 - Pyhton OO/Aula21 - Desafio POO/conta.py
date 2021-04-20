from abc import ABC, abstractclassmethod, abstractproperty


class Conta(ABC):

    @abstractclassmethod
    def __init__(self, agencia, numero, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    # Getter
    @abstractproperty
    @property
    def agencia(self):
        return self.__agencia

    @abstractproperty
    @property
    def numero(self):
        return self.__numero

    @abstractproperty
    @property
    def saldo(self):
        return self.__saldo

    # Getter
    @abstractproperty
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @abstractproperty
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @abstractproperty
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @abstractclassmethod
    def depositar(self):
        pass

    @abstractclassmethod
    def sacar(self):
        pass
