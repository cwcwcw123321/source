# 显示控件提示信息
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self, parent=None):
        super(TooltipForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(700, 250, 550, 550)
        self.setWindowTitle('设置控件提示消息')

        # #添加按钮
        # self.btn=QPushButton('我的按钮')
        # self.btn.setToolTip('这是一个按钮')
        # layout=QHBoxLayout()
        # layout.addWidget(self.btn)
        # mainFrame=QWidget()
        # mainFrame.setLayout(layout)
        # self.setCentralWidget(mainFrame)

        # 添加按钮

        self.btn = QPushButton(self)
        # self.btn.move(100,100)
        self.btn.setText('点击按钮')
        self.btn.setToolTip('这是一个按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TooltipForm()
    w.show()
    sys.exit(app.exec_())
