from PyQt5.QtWidgets import QMainWindow
from templateComboBox import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.comboBox.activated.connect(self.mostraComboBox)

    def mostraComboBox(self):
        self.lineEdit.setText(self.comboBox.currentText())