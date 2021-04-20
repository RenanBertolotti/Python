from pessoa import Produto
from celular import Celular
from teclado import Teclado
from cachorro import Cachorro


prod1 = Produto("camiseta", 50.00)
prod1.desconto(10)

print(prod1.preco)


prod2 = Produto("caneca", 15)
prod2.desconto(10)
print(prod2.preco)

prod1.nome = "renan"
print(prod1.nome)


cel = Celular("Xiaomi", "PocoX3", 4, 128)
print(cel.marca)
print(cel.modelo)
print(cel.ram)
print(cel.memoria)

teclado = Teclado("Logitech", "502", 102, True)

print("----------------------")
print(teclado.marca)
print(teclado.modelo)
print(teclado.n_teclas)
print(teclado.mecanico)

cachorro = Cachorro("Banze", "Salsicha", "Caramelho", 18)
print("----------------------")
print(cachorro.nome)
print(cachorro.raca)
print(cachorro.cor)
print(cachorro.idade)