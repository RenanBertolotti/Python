from conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if not isinstance(valor, (int,float)):
            print("O valor do saque precise ser numerico")
        else:
            if valor > self._saldo:
                print("Não é possivel sacar mais que o saldo da conta")
            else:
                self._saldo -= valor
