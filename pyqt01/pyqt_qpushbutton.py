import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # -> None 의미: return 값이 없다
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 폼의 가로, 세로
        self.setWindowTitle('QPushbutton')
        self.show()

    def addControls(self) -> None:
        self.label = QLabel('메시지: ',self)
        self.label.setGeometry(10,10,600,40)
        self.btn1 = QPushButton('Click',self)
        self.btn1.setGeometry(510,350,120,40)
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널연결

    # event = signal (python)
    def btn1_clicked(self):
        # QMessageBox.information(self, 'signal','btn_clicked') #일반정보
        # QMessageBox.warning(self, 'signal','btn_clicked') # 경고창
        self.label.setText('메시지: btn1 버튼 클릭!')
        QMessageBox.critical(self, 'signal','btn_clicked') #에러창

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins =  qTemplate()
    app.exec_()