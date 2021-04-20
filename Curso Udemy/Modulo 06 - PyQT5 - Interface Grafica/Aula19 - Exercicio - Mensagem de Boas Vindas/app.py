from PyQt5.QtWidgets import QMainWindow
from seunome import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.enviar)

    def enviar(self):
        self.label.setText("Bem Vindo" + " " + self.lineEdit.text())