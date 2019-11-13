# QDesktopWidget
# 通过代码来让窗口居中
import sys
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class centerForm(QMainWindow):
    def __init__(self,parent=None):
        super(centerForm,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('让窗口居中')
        #设置窗口的尺寸
        self.resize(600,360)
        #self.move(100,100)
        self.center()
    def center(self):
        #获取屏幕坐标系
        screen=QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size=self.geometry()
        newLeft = (screen.width()-size.width())/2
        newtop = (screen.height() - size.height()) / 2

        self.move(newLeft,newtop)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = centerForm()
    main.show()
    sys.exit(app.exec_())