from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente


cp = ContaPoupanca(1739, 2201802138, 500.00)
cp.sacar(500)

print(cp.saldo)
cp.depositar(1000.50)
cp.detalhes()

print("#############################")

cc = ContaCorrente(1535, 2222222222, 1000.00)
cc.detalhes()
cc.sacar(1000.00)
cc.sacar(50.00)
cc.sacar(51.00)
cc.depositar(1000.00)