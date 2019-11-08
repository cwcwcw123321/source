import sys
import ui_4
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_4.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())