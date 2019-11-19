'''
QTextEdit控件
'''

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')
        self.resize(300,320)

        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHtml = QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHtml = QPushButton('获取HTML')

        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToHtml)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonTest)
        self.buttonHtml.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToTest)
        self.buttonToHtml.clicked.connect(self.onClick_ButtonToHTML)

    def onClick_ButtonTest(self):
        self.textEdit.setPlainText('hello world ')

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello World </font>')

    def onClick_ButtonToTest(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QTextEditDemo()
    w.show()
    sys.exit(app.exec_())
