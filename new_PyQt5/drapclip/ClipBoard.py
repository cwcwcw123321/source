'''
使用剪贴板
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ClipBoard(QDialog):
    def __init__(self):
        super().__init__()
        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textlabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        # self.imageLabel.setPixmap(QPixmap('./images/book1.png'))

        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(imagePasteButton, 1, 1)
        layout.addWidget(htmlPasteButton, 1, 2)

        layout.addWidget(self.textlabel, 2, 0, 1, 2)  # 控件名，行，列，占用行数，占用列数
        layout.addWidget(self.imageLabel, 2, 1, 1, 2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteHtml)

        self.setWindowTitle('剪贴板')

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('Hello world!')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textlabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images/book.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())  # 从剪贴版获得图像

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textlabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ClipBoard()
    w.show()
    sys.exit(app.exec_())
