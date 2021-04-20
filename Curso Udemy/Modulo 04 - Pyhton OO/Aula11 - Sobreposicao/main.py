from pessoa import Pessoa
from cliente import Cliente
from clientevip import ClienteVip


c1 = Cliente("Renan", 23)
c1.comprar()

print()

c2 = ClienteVip("Ivan", 23, "Bunda-Mole")
c2.comprar()
c2.falar()
print(c2.apelido)