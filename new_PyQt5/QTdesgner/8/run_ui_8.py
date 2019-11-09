#热键的关联
import ui_8
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_8.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())