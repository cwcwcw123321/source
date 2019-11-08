import ui_10
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_10.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())