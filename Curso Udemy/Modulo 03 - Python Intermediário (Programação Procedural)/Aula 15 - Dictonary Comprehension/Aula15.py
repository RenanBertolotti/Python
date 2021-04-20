"""
Dictionary COmprehension - sao utilizadas para otimizaçao(performance) e escrever menos
"""

lista = [
    ("chave1", "Renan"),
    ("chave2", "Maria"),
]

d1 = {x : y for x,y in lista}
#ou
d1 = dict(lista)


d1 = {y:x for x,y in lista}
d1 = {x: y*2 for x,y in lista}
d1 = {x: y.upper() for x,y in lista}
d1 = {x for x in range(5)}
d1 = {f"cahve_{x}": x**2 for x in range(5)}

print(d1)

