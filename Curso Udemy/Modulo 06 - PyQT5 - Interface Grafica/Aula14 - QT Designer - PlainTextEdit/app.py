from PyQt5.QtWidgets import QMainWindow
from plainTextEdit import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.caractere = 0

        # self.plainTextEdit.setPlainText("oi")
        # self.plainTextEdit.setReadOnly(True) - apenas Leitura

        self.pushButton.clicked.connect(self.text)

        self.plainTextEdit.textChanged.connect(self.mudou)
        self.plainTextEdit.setUndoRedoEnabled(False) # para retirar o Control Z - Control Y

    def text(self):
        self.plainTextEdit.appendPlainText("Ola mundo")

    def mudou(self):
        valor = len(self.plainTextEdit.toPlainText())

        print(valor)
