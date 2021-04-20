from PyQt5.QtWidgets import QMainWindow
from untitled import Ui_MainWindow
from app2 import App2


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.jan2 = App2("ola mundo")

        self.pushButton.clicked.connect(self.mudajanela)

    def mudajanela(self):
        self.jan2.show()
        # self.hide() - esconde a janela principal