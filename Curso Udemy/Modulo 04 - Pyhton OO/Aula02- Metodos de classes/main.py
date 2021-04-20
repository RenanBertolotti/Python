from pessoa import Pessoa

p1 = Pessoa("Renan", 22)

print(p1)
print(p1.nome)
p1.getAnoNascimento()
print(p1.idade)


print("-------------------\n")


p2 = Pessoa.porAnoNascimento("Ivan", 25)
print(p2)
print(p2.idade)
p2.getAnoNascimento()