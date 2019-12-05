'''
使用打印机
'''

import sys
from PyQt5 import QtCore,QtPrintSupport,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class PrintSupport(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,300,300)

        self.button=QPushButton('打印QtextEdit控件中的内容',self)
        # self.button.setGeometry(20,20,260,30)
        self.editor=QTextEdit('默认文本',self)
        self.editor.move(20,80)
        # self.setGeometry(20,60,260,200)

        self.button.clicked.connect(self.print)

    def print(self):
        printer=QtPrintSupport.QPrinter()

        painter=QtGui.QPainter()
        #将绘制的目标重定向到打印机
        painter.begin(printer)#本来是self 是当前窗口
        screen=self.editor.grab()   #获得可视屏幕
        painter.drawPixmap(10,10,screen)
        painter.end()
        print('print')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=PrintSupport()
    w.show()
    sys.exit(app.exec_())
