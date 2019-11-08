import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import ui_2

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui= ui_2.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())