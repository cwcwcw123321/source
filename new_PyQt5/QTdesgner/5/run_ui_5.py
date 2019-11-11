import ui_5
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_5.Ui_MainWindow()
    ui.setupUi(w)
    w.show()

    sys.exit(app.exec_())