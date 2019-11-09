# 学习为窗口添加工具栏
import ui_11
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 设置高清屏幕属性  ？？   设置出来界面显示正常
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_11.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
