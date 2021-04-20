from untitled import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.radioButton.toggled.connect(self.selecionar)
        self.radioButton_2.toggled.connect(self.selecionar)
        self.radioButton_3.toggled.connect(self.selecionar)

    def selecionar(self):
        radioSelecionado = self.sender()
        self.lblSaida.setText(radioSelecionado.text())