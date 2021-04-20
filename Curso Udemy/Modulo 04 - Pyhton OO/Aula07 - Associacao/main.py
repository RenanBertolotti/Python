from escritor import Escritor
from caneta import Caneta
from maquinaescrever import MaquinaEscrever

caneta = Caneta("Bic")
escritor = Escritor("Renan")
maquina = MaquinaEscrever("Cassio")

print(escritor.nome)
print(caneta.marca)
print(maquina.marca)

maquina.escrever()
caneta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

