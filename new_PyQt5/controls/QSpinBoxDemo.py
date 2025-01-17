'''
计数器控件（QSpinBox）
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(300,100)

        layout=QVBoxLayout()
        self.label=QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb=QSpinBox()
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值'+str(self.sb.value()))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QSpinBoxDemo()
    w.show()
    sys.exit(app.exec_())