"""
Pilhas e filas
Pilha (stack) - LIFO - Last In Fist Out.
    Exemplo: Pilha de livros que sao adicionados um sobre o outro
Fila (queue) - FIFO - Fist In Firts Out.
    Exemplo: Uma fila de banco (Ou qualquer fila da vida real).
Filas pode ter efeitos coleterais em desempenho, porque a cada item alterado, todos os indices serao modificados.
"""

################ LISTA ##########################
"""
livros = list()
livros.append("Livro 1")
livros.append("Livro 2")
livros.append("Livro 3")
livros.append("Livro 4")
livros.append("Livro 5")

livro_removido = livros.pop() #Remove o ultimo elemento da lista "5"
livro_removido = livros.pop() #Remove o ultimo elemento da lista "4"
livro_removido = livros.pop() #Remove o ultimo elemento da lista "3"
livro_removido = livros.pop() #Remove o ultimo elemento da lista "2"
livro_removido = livros.pop() #Remove o ultimo elemento da lista "1"

print(livros)
print(livro_removido)

"""
######## FILA ##############
from collections import deque

fila = deque()
#Caso queira, voce pode deixar uma fila com numero limitado, ficando:
#fila = deque(maxlen=5)

fila.append("Joao")
fila.append("Maria")
fila.append("Eu")
fila.append("Marcos")
fila.append("Jose")

print(f"item removido: {fila.popleft()}")
print(f"item removido: {fila.popleft()}")

for nome in fila:
    print(nome)
