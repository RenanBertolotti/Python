"""
Operadores Logicos
and, or, not
in e not in
"""
a = 2
b = 2
c = 3

nome = "luiz otavio"

if "renan" not in nome:
    print("nao existe o texto")

if 'u' in nome:
    print("existe a letra U no seu nome")

if a == b and b < c:
    print("verdadeiro")

if a == b or b < c:
    print("verdadeiro")

if a == b and not b > c:
    print("falso")

if not a:
    print("por favor, preencha A")
