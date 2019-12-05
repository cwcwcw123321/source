'''
创建和使用工具栏
工具栏默认按钮：只显示图标，将文本作为悬停提示展示
工具栏按钮有三种显示状态
1、只显示图标
2、只显示文本
3、同时显示图标文本
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Toolbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)

        tb1=self.addToolBar('file')

        new=QAction(QIcon('./images/new.png'),'new',self)
        tb1.addAction(new)

        open=QAction(QIcon('./images/open.png'),'open',self)
        tb1.addAction(open)

        save=QAction(QIcon('./images/save.png'),'open',self)
        tb1.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb2=self.addToolBar('file1')
        new1 = QAction(QIcon('./images/new.png'), '新建', self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)

        tb2.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self,a):
        print('按下的工具栏按钮是：',a.text())




if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=Toolbar()
    w.show()
    sys.exit(app.exec_())
