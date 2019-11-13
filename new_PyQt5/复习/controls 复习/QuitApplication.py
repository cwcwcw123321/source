import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class QuitApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('退出应用程序')
        self.resize(400,400)
        self.initUI()
    def initUI(self):
        self.btn=QPushButton(self)
        self.btn.setText('退出程序')
        self.btn.move(175,180)
        self.btn.clicked.connect(self.close)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QuitApplication()
    w.show()
    sys.exit(app.exec_())
