'''
滑块控件(QSlider)
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,100)

        layout=QVBoxLayout()
        self.label=QLabel('你好，PyQt5 ')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        #滑块支持水平，垂直
        self.slider=QSlider(Qt.Horizontal)  #水平
        #设置最小值
        self.slider.setMinimum(12)
        #设置最大值
        self.slider.setMaximum(48)
        #步长
        self.slider.setSingleStep(3)
        #设置当前值
        self.slider.setValue(18)
        #设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        #设置刻度间隔
        self.slider.setTickInterval(6)

        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)
        self.setLayout(layout)
        self.resize(700,400)

    def valueChange(self):
        print('当前值：{}'.format(self.slider.value()))
        size=self.slider.value()
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = SliderDemo()
    main.show()
    sys.exit(app.exec_())

