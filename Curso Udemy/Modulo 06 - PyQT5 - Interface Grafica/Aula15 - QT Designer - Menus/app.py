from PyQt5.QtWidgets import QMainWindow
from menus import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.menuArquivo.triggered.connect(self.selecionado)
        self.actionSalvar.triggered.connect(self.salvaDados)

    def selecionado(self, item):
        print(item.text() + " Foi selecionado")

    def salvaDados(self):
        with open("abc.txt", "w+") as file:
            file.write("linha 1\n")
            file.write("linha 2\n")
            file.write("linha 3\n")

            file.seek(0, 0)
            print(file.read())
