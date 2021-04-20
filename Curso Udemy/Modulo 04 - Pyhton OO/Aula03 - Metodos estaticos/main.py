from pessoa import Pessoa

p1 = Pessoa("Renan", 22)
print(p1)
print(p1.nome)
print(p1.idade)


idade = Pessoa.gera_id()
print(Pessoa.gera_id())