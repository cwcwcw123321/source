'''
树控件(QTreeWidget)的基本用法
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('树控件的基本用法')

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)
        # 指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('./images/root.png'))
        self.tree.setColumnWidth(0, 160)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('./images/bao3.png'))
        # 增加复选框
        child1.setCheckState(0, Qt.Checked)
        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('./iamges/bao6.png'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '新的值')
        child3.setIcon(0, QIcon('./images/music.png'))

        self.tree.expandAll()  # 默认树都是打开的

        self.setCentralWidget(self.tree)  # 设为中心控件  充满整个屏幕


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BasicTreeWidget()
    w.show()
    sys.exit(app.exec_())
