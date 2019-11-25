'''
对话框:QDialog
QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.btn=QPushButton(self)
        self.btn.setText('弹出对话框')
        self.btn.move(50,50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog=QDialog()
        button1=QPushButton('确定',dialog)
        button1.clicked.connect(dialog.close)
        button1.move(50,50)
        dialog.setWindowTitle('')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QDialogDemo()
    w.show()
    sys.exit(app.exec_())