from checkbox import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.checaMarcado)

        self.checkBox_2.stateChanged.connect(self.mudatitulo)


    def mudatitulo(self):
        if self.checkBox_2.isChecked() is True:
            self.setWindowTitle("Voce mudou")
        else:
            self.setWindowTitle("Main WIndos")

    def checaMarcado(self):
        if self.checkBox.isChecked() is True:
            self.setGeometry(400, 150, 500, 500)
            print(self.checkBox.text())
        else:
            print("desmarcado")
            self.setGeometry(200, 150, 500, 500)