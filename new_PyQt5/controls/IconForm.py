import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

'''
窗口的setWindowIcon方法用于设置窗口的图标，只在windows中可用
QApplication中的setWindowIcon方法就只能设置应用程序的图标了
'''


class IconForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口图标
        self.setWindowIcon(QIcon('./images/Basilisk.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())
