# 复习QLineEdit

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit1=QLineEdit()
        #使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',23))

        edit2=QLineEdit()
        #使用浮点校验器
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4=QLineEdit()
        edit4.textChanged.connect(self.Changed)

        edit5 = QLineEdit()
        # edit5.setEchoMode(QPasswordDigestor)
        edit5.setEchoMode(QLineEdit.Password)

        edit6 = QLineEdit('hello pyqt5')
        edit6.setReadOnly(True)

        formLayout=QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验', edit2)
        formLayout.addRow('input Mask', edit3)
        formLayout.addRow('文本改变信号', edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读', edit6)

        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合示例')

    def Changed(self,text):
        print(text)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QLineEditDemo()
    w.show()
    sys.exit(app.exec_())
