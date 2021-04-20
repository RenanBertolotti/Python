from PyQt5.QtWidgets import QMainWindow
from templateLineEdit import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.mostraDisplay)

    def mostraDisplay(self):
        self.lineEdit2.setText(self.lineEdit.text())