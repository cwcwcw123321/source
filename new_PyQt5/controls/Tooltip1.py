from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("今天是第一天这么较真__init__(*,parent=None)这个问题")
        self.setWindowTitle('问题复检')
        self.setGeometry(700,350,500,500)
        #添加按钮

        btn=QPushButton(self)
        btn.setText('按钮')
        btn.setToolTip("这是一个按钮")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=Example()
    w.show()
    sys.exit(app.exec_())