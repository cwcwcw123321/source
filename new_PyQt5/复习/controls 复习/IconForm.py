import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class IconForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置窗口图标')
        self.setGeometry(400,400,350,350)
        self.setWindowIcon(QIcon('./images/Banshee.ico'))

app=QApplication(sys.argv)
w=IconForm()
w.show()
sys.exit(app.exec_())
