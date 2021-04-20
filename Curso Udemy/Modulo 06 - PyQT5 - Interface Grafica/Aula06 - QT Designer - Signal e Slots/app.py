from template import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButtonCopiar.clicked.connect(self.adicionar)

    def adicionar(self):
        self.LineEditColar.setText(self.LineEditColar.text() + self.pushButtonColar.text() + "1")