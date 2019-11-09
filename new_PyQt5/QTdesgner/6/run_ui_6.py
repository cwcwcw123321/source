from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import ui_6

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QMainWindow()
    ui=ui_6.Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
