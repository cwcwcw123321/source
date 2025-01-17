'''
用掩码限制QLineEdit控件的输入
A   ASCII字母字符是必须输入的（A-Z、a-z）
a   ASCII字母符字是允许输入的，但不是必须的（A-Z、a-z）
N   ASCII字母字符是必须输入的（A-Z、a-z、0-9）
n   ASCII字母符字是允许输入的，但不是必须的（A-Z、a-z、0-9）
X   任何字符都是必须输入的
x   任何字符是允许输入的，但不是必须的
9   ASCII数字字符是必须输入的（0-9）
0   ASCII数字符字是允许输入的，但不是必须的（0-9）
D   ASCII数字字符是必须输入的（1-9）
d   ASCII数字字符是允许输入的，但不是必须的（1-9）
#   ASCII数字字符或加减符是允许输入的，但不是必须的
H   十六进制式字符是必须输入的（0,1）
h   十六进制式字符是允许输入的，但不是必须的（0,1）
>   所有的字母字符都大写
<   所有的字母字符都小写
！   关闭大小写转换
\   使用“\”转义上面列出的字符
'''

from PyQt5.QtWidgets import *
import sys


class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        # 创建框架
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dataLineEdit = QLineEdit()
        licenselLineEdit = QLineEdit()
        # 192.168.21.45
        ipLineEdit.setInputMask('000.000.000.000;_')  # 不输入显示_
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dataLineEdit.setInputMask('0000-00-00')
        licenselLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码', ipLineEdit)
        formLayout.addRow('mac掩码', macLineEdit)
        formLayout.addRow('日期掩码', dataLineEdit)
        formLayout.addRow('许可证掩码', licenselLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QLineEditMask()
    w.show()
    sys.exit(app.exec_())
