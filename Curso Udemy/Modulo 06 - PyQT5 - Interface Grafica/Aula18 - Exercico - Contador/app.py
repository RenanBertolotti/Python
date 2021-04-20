from PyQt5.QtWidgets import QMainWindow
from contador import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.contador = 0

        self.btnDecrementar.clicked.connect(self.decrementar)
        self.btnAcrescentar.clicked.connect(self.acrescentar)

    def decrementar(self):
        self.contador -= 1
        self.lineEdit.setText(str(self.contador))

    def acrescentar(self):
        self.contador += 1
        self.lineEdit.setText(str(self.contador))