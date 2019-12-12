'''
设置单元格的文本对齐方式
setTextAlignment
Qt.alignRight 等

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CellTextAlignment(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('设置单元格的文本对齐方式')
        self.resize(430,230)
        layout=QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        newItem=QTableWidgetItem('雷神')
        newItem.setTextAlignment(Qt.AlignRight |Qt.AlignBottom)
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.tableWidget.setItem(0,1, newItem)

        newItem = QTableWidgetItem('190')
        newItem.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(0,2, newItem)




        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=CellTextAlignment()
    w.show()
    sys.exit(app.exec_())