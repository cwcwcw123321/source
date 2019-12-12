'''
合并单元格
setSpan(row,col,要合并的行数，要合并的列数)
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Span(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('合并单元格')
        self.resize(430,230)
        layout=QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','身高'])

        newItem=QTableWidgetItem('雷神')
        self.tableWidget.setItem(0,0,newItem)
        self.tableWidget.setSpan(0,0,3,1)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1, newItem)
        self.tableWidget.setSpan(0,1,2,1)

        newItem = QTableWidgetItem('190')
        self.tableWidget.setItem(0,2, newItem)
        self.tableWidget.setSpan(0,2,4,1)

        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=Span()
    w.show()
    sys.exit(app.exec_())