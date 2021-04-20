from trocarjanela import Ui_Janela2
from PyQt5.QtWidgets import QMainWindow


class App2(QMainWindow, Ui_Janela2):
    def __init__(self, mensagem, parent=None,):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.setText(mensagem)

        self.pushButton.clicked.connect(self.fechar)

    def fechar(self):
        self.close()