from PyQt5.QtWidgets import QMainWindow
from olamundo import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)

        self.pushButton.clicked.connect(self.geraOlaMundo)

    def geraOlaMundo(self):
        linguagem = self.comboBox.currentText()

        if linguagem == "Pyhton":
            self.plainTextEdit.setPlainText(self.python())
        elif linguagem == "Java":
            self.plainTextEdit.setPlainText(self.java())
        elif linguagem == "C++":
            self.plainTextEdit.setPlainText(self.c_mais_mais())

    def python(self):
        return 'print("Ola Mundo")'

    def java(self):
        return 'System.out.println(“Hello world”)'

    def c_mais_mais(self):
        return 'std::cout << “Hello world” << std::endl'
