from novo import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.botao1.clicked.connect(self.acao_botao1)
        self.botao2.clicked.connect(self.acao_botao2)

    def acao_botao1(self):
        #nomeBotao = self.botao1.text()

        if self.botao1.text() == "Mudou Aqui":
            self.botao1.setText("Clique Aqui")
        else:
            self.botao1.setText("Mudou Aqui")

        self.nomeBotao = self.botao1.text()
        print(self.nomeBotao)

    def acao_botao2(self):
        exit()