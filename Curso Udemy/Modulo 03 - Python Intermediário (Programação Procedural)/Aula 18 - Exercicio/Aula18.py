#SOmando a partir de uma lista, usando a list Comprehension

carrinho = []

carrinho.append(("produto1", 20))
carrinho.append(("produto2", 30))
carrinho.append(("produto3", 50))

soma = sum([valor for i,valor in carrinho])

print(soma)

""" TESTE 1 - DEU CERTO!!! 
soma = 0
for i,valor in carrinho:
    soma += valor

print(soma)
"""

