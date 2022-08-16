import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결
       

    def btn1_clicked(self):
        self.label.setText('메시지 : btn1 버튼 클릭!!!')
        QMessageBox.information(self, 'signal', 'btn1_clicked!!')

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()