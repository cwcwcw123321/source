import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Tooltip(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('为控件添加提示')
        self.setWindowIcon(QIcon('./images/Air Elemental.ico'))
        self.setToolTip('今天是星期3')
        self.setGeometry(600,400,550,350)

        self.btn=QPushButton(self)
        self.btn.setToolTip('这是一个按钮')
        self.btn.setText('点击我')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=Tooltip()
    w.setWindowIcon(QIcon('./images/Fire Elemental.ico'))
    w.show()
    sys.exit(app.exec_())