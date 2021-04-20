from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print("O valor de saque precisa ser INT ou FLOAT")
        else:
            if valor > self._saldo:
                if valor > (self.saldo + self._limite):
                    print("Voce nao pode sacar mais que o limite da sua conta")
                else:
                    print("Voce está utilizando o seu limite")
                    self._saldo -= valor
                    self.detalhes()
            else:
                self._saldo -= valor
                self.detalhes()