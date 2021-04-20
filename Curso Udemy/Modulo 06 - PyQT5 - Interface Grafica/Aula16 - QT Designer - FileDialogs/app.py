from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from menus import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.actionTexto.triggered.connect(self.abrirTexto)
        self.actionPython.triggered.connect(self.abrirArquivos)
        self.actionSalvar.triggered.connect(self.salvar)

    def abrirTexto(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "abrir um arquivo de Texto", r"C\\", "Arquivos de texto (*.txt)")
        print(caminho)

        try:
            with open(caminho, 'r') as file:
                info = file.read()
                self.plainTextEdit.setPlainText(info)
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("ERRO")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Arquivo invalido")
            msg.setInformativeText("O arquivo selecionado não é um .txt")

            msg.exec_()
            print("Arquivo invalido")

    def abrirArquivos(self):
        caminho, _ = QFileDialog.getOpenFileNames(self,
                                                  "abrir um arquivo de Texto",
                                                  r"C\\",
                                                  "Arquivos de texto (*.txt)")
        print(caminho)

        try:
            with open(caminho[0], 'r') as file:
                info = file.read()
                self.plainTextEdit.setPlainText(info)

            with open(caminho[1], "r") as file:
                info = file.read()
                self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText() + "\n\n" + info)
        except Exception as e:
            print(e)

    def salvar(self):
        conteudo = self.plainTextEdit.toPlainText()

        caminho, _ = QFileDialog.getSaveFileName(self, "Salvar")
        print(caminho)

        with open(caminho, 'w') as file:
            file.write(conteudo)

