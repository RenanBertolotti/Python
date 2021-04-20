from cliente import Cliente


class ClienteFisico(Cliente):
    def __str__(self):
        return f"{self.nome} , {self.idade}, {self.telefone}, {self.email}, {self.cpf}"
