import sys
from new_PyQt5 import ui_first
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ =='__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui= ui_first.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())

