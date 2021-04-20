"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from banco import Banco
from clientefisico import ClienteFisico
from clientejuridico import ClienteJuridico
from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente


cliente1 = ClienteFisico("Renan", 22, 19997204108, "renanbertolotti@gmail.com", "443.063.478-50")
cliente2 = ClienteFisico("Ivan", 23, 1938953111, "ivanbertolotti@gmail.com", "443.563.918-30")
cliente3 = ClienteFisico("Maria", 17, 1938952202, "mariaferraz@gmail.com", "113.453.376-56")
cliente4 = ClienteJuridico("Renan", 22, 19997204108, "renanbertolotti@gmail.com", "113.453.376-56", "01.123.456.789/0001-10", "Pink Uzi")

print("CLIENTES :")
print(cliente1)
print(cliente2)
print(cliente3)
print(cliente4)
print("\n")


cp1 = ContaPoupanca(1739, 122354, 1000.00, cliente1)
cp2 = ContaPoupanca(1739, 135411, 500.00, cliente2)
cp3 = ContaCorrente(1739, 123456, 100.00, cliente3)

print("Contas :")
print(cp1)
print(cp2)
print(cp3)
print("\n")

cp1.sacar(500.00)
cp2.sacar(550.00)
cp3.sacar(201.00)



banco = Banco("Bradesco")
print("Contas de banco:")
banco.conta = cp1
banco.conta = cp2
banco.conta = cp3
banco.listaContas()

