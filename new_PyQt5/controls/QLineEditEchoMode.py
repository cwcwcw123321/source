'''
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode（回显模式）
4中回显模式：
    1、Normal    正常模式
    2、NoEcho    不回显 输入信息不显示在屏幕上
    3、Password  密码
    4、PasswordEchoNEdit     先显示输入然后变为密码
'''

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout=QFormLayout()#创建表单布局

        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordEchoOnEditLineEdit=QLineEdit()

        formLayout.addRow('Normal',normalLineEdit)
        formLayout.addRow('NoEcho', noEchoLineEdit)
        formLayout.addRow('password', passwordLineEdit)
        formLayout.addRow('passwordEchoEdit', passwordEchoOnEditLineEdit)

        #placeholdtext 灰色提示

        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QLineEditEchoMode()
    w.show()
    sys.exit(app.exec_())