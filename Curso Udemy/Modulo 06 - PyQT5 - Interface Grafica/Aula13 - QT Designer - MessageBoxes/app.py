from PyQt5.QtWidgets import QMainWindow, QMessageBox
from messageBox import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.caixas)

    def caixas(self):
        msg = QMessageBox()
        msg.setWindowTitle("Caixa!")
        msg.setText("Caixa criada")

        msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QMessageBox.Question)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Critical)

        msg.setInformativeText("Informação extra")

        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.No)
        msg.setEscapeButton(QMessageBox.Cancel)

        msg.setDetailedText("Mais informaçoes")

        msg.buttonClicked.connect(self.resultado)

        return msg.exec_()

    def resultado(self, clicado):
        if clicado.text() == "&No":
            print("Botao clickado = No")
        elif clicado.text() == "&Yes":
            print("Botao clickado = Yes")
        elif clicado.text() == "Cancel":
            print("Botao clikado = Cancel")
