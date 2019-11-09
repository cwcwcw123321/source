import sys
import ui_3
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui= ui_3.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())