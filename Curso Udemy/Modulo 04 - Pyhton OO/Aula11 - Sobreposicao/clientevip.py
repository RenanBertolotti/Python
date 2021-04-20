from cliente import Cliente


class ClienteVip(Cliente):
    def __init__(self, nome, idade, apelido):
        super().__init__(nome,idade)
        self.apelido = apelido

    def falar(self):
        super().falar()
        print("ClasseVip esta falando")
