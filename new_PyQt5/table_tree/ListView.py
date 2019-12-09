'''
显示列表数据（QListView控件）
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
import sys

class ListViewDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListview 例子')
        self.resize(300,270)
        layout=QVBoxLayout()

        listview=QListView()
        listModel=QStringListModel()
        self.list=['列表项目1','列表项目2','列表项目3']

        listModel.setStringList(self.list)
        listview.setModel(listModel)
        listview.clicked.connect(self.click)
        layout.addWidget(listview)

        self.setLayout(layout)

    def click(self,item):
        QMessageBox.information(self,'QListView','您选择了：'+self.list[item.row()])







if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=ListViewDemo()
    w.show()
    sys.exit(app.exec_())