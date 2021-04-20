from eletronico import Eletronico
from log import LogMixin


class SmartPhone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            info = f"{self.nome} nao esta ligado"
            print(info)
            self.log_info(info)
        else:
            if self._conectado:
                info = f"{self.nome} ja esta conectado."
                print(info)
                self.log_info(info)
            else:
                self._conectado = True
    
    def desconectar(self):
        if self._conectado:
            self._conectado = False
        else:
            info = f"{self.nome} ja esta conectado."
            print(info)