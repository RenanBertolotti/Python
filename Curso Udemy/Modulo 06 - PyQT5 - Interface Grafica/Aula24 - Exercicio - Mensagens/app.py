from PyQt5.QtWidgets import QMainWindow,QMessageBox
from mensagens import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.mensagem)

    def mensagem(self):
        if self.checkBox.isChecked():
            messageBox = QMessageBox()

            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("Mensagem de Erro")
            messageBox.setInformativeText(self.lineEdit.text())

            messageBox.exec_()
        else:
            messageBox = QMessageBox()

            messageBox.setIcon(QMessageBox.Information)
            messageBox.setText("Mensagem de aviso")
            messageBox.setInformativeText(self.lineEdit.text())

            messageBox.exec_()