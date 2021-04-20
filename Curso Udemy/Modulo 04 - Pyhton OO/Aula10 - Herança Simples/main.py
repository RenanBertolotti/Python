from cliente import Cliente
from aluno import Aluno

cliente1 = Cliente("Renan", 22)

print(cliente1.nome, cliente1.idade)
cliente1.falar()

aluno1 = Aluno("Ivan", 32)
aluno1.falar()
