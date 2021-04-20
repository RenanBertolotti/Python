from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, telefone, email, cpf):
        super().__init__(nome, idade)
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf

    # Getter
    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @ property
    def cpf(self):
        return self.__cpf

    # Setter
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @email.setter
    def email(self, email):
        self.__email = email

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf