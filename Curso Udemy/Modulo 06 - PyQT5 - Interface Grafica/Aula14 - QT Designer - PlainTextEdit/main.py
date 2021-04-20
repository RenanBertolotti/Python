import sys
from PyQt5.QtWidgets import QApplication
from app import App


application = QApplication(sys.argv)
app = App()

app.show()
application.exec_()