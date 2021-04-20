class Pessoa():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"({self.nome}" + "," + f"{self.telefone})"