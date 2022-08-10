import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import *
# from PyQt5.QtGui import QPainter, QColor, QFont
# from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # -> None 의미: return 값이 없다
        super().__init__()
        self.initUI()

    # 화면 정의를 위해 만든 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 폼의 가로, 세로
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png'))  # 윈도우 아이콘 지정
        label1 = QLabel('',self)
        label2 = QLabel('',self)
        label1.setStyleSheet(
            ('border-width: 3px;'
             'border-style: solid;'
             'border-color: blue;'
             'image: url(./pyqt01/image/image1.png)')
        )
        label2.setStyleSheet(
            ('border-width: 3px;'
             'border-style: dot-dot-dash;'
             'border-color: red;'
             'image: url(./pyqt01/image/image2.png)')
        )

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins =  qTemplate()
    app.exec_()