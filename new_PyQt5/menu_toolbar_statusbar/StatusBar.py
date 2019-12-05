'''
创建和使用状态栏
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('状态栏演示')
        self.resize(300,200)

        bar=self.menuBar()
        file=bar.addMenu('file')
        file.addAction('show')
        file.triggered.connect(self.processTrigger)#triggered 触发

        self.setCentralWidget(QTextEdit())
        self.statusBar=QStatusBar()

        self.setStatusBar(self.statusBar)


    def processTrigger(self,q):
        if q.text()=='show':
            self.statusBar.showMessage(q.text()+'菜单被点击了',5000)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=StatusBar()
    w.show()
    sys.exit(app.exec_())
