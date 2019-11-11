'''
QLabel与伙伴控件
mainLayout.addWidget(空间对象,rowIndex,columnIndex,row,column)  控件位置，控件尺寸
'''

import sys
from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控制')

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        #设置伙伴空间
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴空间
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK=QPushButton('&Ok')
        btnCancel=QPushButton('&Cancel')

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0,1,1)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0,1,1)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1,1,1)
        mainLayout.addWidget(btnCancel,2,2,1,1)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QLabelBuddy()
    w.show()
    sys.exit(app.exec_())