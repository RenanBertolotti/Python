"""
List COmprehension - sao utilizadas para otimizaçao(performance) e escrever menos
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
l3 = [variavel * 2 for variavel in l1]
l4 = [(variavel, variavel2) for variavel in l1 for variavel2 in range(3)]

l5 = ["Renan", "Ana", "Maria"]
l6 = [valor.replace('a',"@").upper() for valor in l5]


tupla = (
    ("chave", "valor"),
    ("chave2", "valor2"),
)
l7 = [(y, x) for x, y in tupla]  #inverte os valores


l8 = list(range(100))
l9 = [variavel for variavel in l8 if variavel%3==0 if variavel%8==0]

l10 = [variavel if variavel%3==0 else f"não é{variavel}" for variavel in l3]
print(l10)