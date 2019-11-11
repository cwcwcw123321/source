import ui_5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置高清屏幕属性  ？？   设置出来界面显示正常
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_5.Ui_MainWindow()
    ui.setupUi(w)
    w.show()

    sys.exit(app.exec_())