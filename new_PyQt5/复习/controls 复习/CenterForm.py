import sys
from PyQt5.QtWidgets import *


class CenterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口居中')
        self.resize(260, 160)
        self.initUI()

    def initUI(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        print(screen)
        size = self.geometry()
        left = (screen.width() - size.width()) / 2
        right = (screen.height() - size.height()) / 2
        self.move(left, right)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CenterForm()
    w.show()
    sys.exit(app.exec_())
