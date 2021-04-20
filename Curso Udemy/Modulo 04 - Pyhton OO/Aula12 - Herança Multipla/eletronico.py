from log import LogMixin


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def ligar(self):
        if not self._ligado:
            self._ligado = True
        else:
            info = "O aparelho já está ligado"
            self.write(info)
            print(info)

    def desligar(self):
        if not self._ligado:
            print("O aparelho já está desligado")
            return
        else:
            self._ligado = False
