'''
在单元格中放置控件
setItem： 将文本放到单元格中
setCellWidget:将控件放到单元格中
setStyleSheet：设置控件的样式(QSS)
'''
import sys
from PyQt5.QtWidgets import *

class PlaceControlInCell(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('在单元格中放置控件')
        self.resize(430,300)
        layout=QHBoxLayout()

        tablewidget=QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])
        textItem=QTableWidgetItem('小明')
        tablewidget.setItem(0,0,textItem)

        combox=QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        #QSS
        combox.setStyleSheet('QComboBox{margin:3px};')
        tablewidget.setCellWidget(0,1,combox)

        modifyButton=QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:4px};')
        tablewidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=PlaceControlInCell()
    w.show()
    sys.exit(app.exec_())









