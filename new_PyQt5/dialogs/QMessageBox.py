'''
消息对话框 ：QMessageBox
1、关于对话框
2、错误对话框
3、警告对话框
4、提问\疑问对话框
5、消息对话框

有两点差异
1、显示的对话框图标可能不一样
2、显示的按钮是不一样的

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QMessageBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QMessageBox案例')
        self.resize(300,400)

        layout=QVBoxLayout()
        self.btn1=QPushButton(self)
        self.btn1.setText('显示关于对话框')
        self.btn1.clicked.connect(self.showDialog)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton(self)
        self.btn2.setText('显示消息对话框')
        self.btn2.clicked.connect(self.showDialog)
        layout.addWidget(self.btn2)

        self.btn3 = QPushButton(self)
        self.btn3.setText('显示警告对话框')
        self.btn3.clicked.connect(self.showDialog)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton(self)
        self.btn4.setText('显示错误对话框')
        self.btn4.clicked.connect(self.showDialog)
        layout.addWidget(self.btn4)

        self.btn5 = QPushButton(self)
        self.btn5.setText('显示提问对话框')
        self.btn5.clicked.connect(self.showDialog)
        layout.addWidget(self.btn5)





        self.setLayout(layout)

    def showDialog(self):
        text=self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == '显示消息对话框':
            reply=QMessageBox.information(self, '消息', '这是一个消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            print(reply==QMessageBox.Yes)#判断是不是点击yes
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框',QMessageBox.No|QMessageBox.Yes,QMessageBox.No)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMessageBoxDemo()
    w.show()
    sys.exit(app.exec_())