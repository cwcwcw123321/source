'''
按钮控件（QPushButton）

QAbstractButton
AToolButton
QRadioButton
QCheckBox

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        #垂直布局
        layout=QVBoxLayout()

        self.btn1=QPushButton('第一个按钮')
        self.btn1.setText('First Button1')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda:self.whichButton(self.btn1))
        self.btn1.clicked.connect(self.ButtonState)
        layout.addWidget(self.btn1)
        # 在文本前面显示图标

        self.btn2=QPushButton('图像按钮')
        self.btn2.setIcon(QIcon(QPixmap('./images/python.png')))
        self.btn2.clicked.connect(lambda:self.whichButton(self.btn2))
        layout.addWidget(self.btn2)

        self.btn3=QPushButton('不可用的按钮')
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)
        #第四个默认按钮
        self.btn4=QPushButton('&MyButton')
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda :self.whichButton(self.btn4))
        layout.addWidget(self.btn4)

        self.setLayout(layout)
        self.resize(400,300)
    def ButtonState(self):
        if self.btn1.isChecked():
            print('按钮已被选中')
        else:
            print('按钮未被选中')
    def whichButton(self,i):
        print('被单击的按钮是<'+i.text()+'>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QPushButtonDemo()
    w.show()
    sys.exit(app.exec_())



