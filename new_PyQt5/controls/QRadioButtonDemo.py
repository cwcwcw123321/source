'''
单选按钮控件QRadioButton
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        # 创建水平布局
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        #self.button1.setText('单选按钮1')
        self.button1.setChecked(True)  # 设置默认选中状态

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')



        # if radiobutton.text() == '单选按钮1':
        #     if radiobutton.isChecked() == True:
        #         print('<' + radiobutton.text() + '>被选中')
        #     else:
        #         print('<' + radiobutton.text() + '>位被选中')
        #
        # if radiobutton.text() == '单选按钮2':
        #     if radiobutton.isChecked() == True:
        #         print('<' + radiobutton.text() + '>被选中')
        #     else:
        #         print('<' + radiobutton.text() + '>位被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QRadioButtonDemo()
    w.show()
    sys.exit(app.exec_())
