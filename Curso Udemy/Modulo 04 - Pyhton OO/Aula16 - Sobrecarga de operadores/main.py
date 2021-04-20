"""
No pyhton, o comportamento dos operadores é dfinido por metodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<class "Retangulo({self.x}, {self.y})" > '

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2
print(r3)
print(r1 == r2)