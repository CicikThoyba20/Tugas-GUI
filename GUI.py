import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def main_window():
    app = QApplication(sys.argv)
    main_window = QWidget()
    layout = QHBoxLayout()

    tl = QLabel(main_window)
    tl.setText("Kotak Angka")
    tl.move(50,50)
    for i in range(5):
        button = QPushButton(str(i + 1))
        layout.addWidget(button)
        button.setGeometry(50,50,100,50)
        button.setStyleSheet("font-size: 25%;background-color: grey; color: red")
        button.setFont(QFont('Time New Roman',25))
    main_window.setGeometry(100,100,200,200)
    main_window.setWindowTitle("PyQt5 Example")
    main_window.setLayout(layout)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main_window()
