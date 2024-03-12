import sys
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import QSize, Qt

# class CustomButton(QPushButton):
#     def __init__(self, text):
#         super().__init__(text)
#         self.setMouseTracking(True)
#     def mouseMoveEvent(self, event: QMouseEvent):
#         super().mouseMoveEvent(event)
#         event.ignore()
class MainWindow(QMainWindow):
    button = None

    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)

        self.setWindowTitle('My App')
        self.setGeometry(300, 300, 300, 300)
        self.installEventFilter(self)

        self.label = QLabel(self)
        self.label.resize(200, 40)

        self.button = QPushButton('Pushi-pushi')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.layout().addWidget(self.label)
        self.setCentralWidget(self.button)


    def button_clicked(self):
        self.setWindowTitle('Clicked')
        self.button.hide()

    def mouseMoveEvent(self, event: QMouseEvent):
        self.label.setText('Mouse position: (x: {0}; y: {1})'.format(event.pos().x(), event.pos().y()))

    def keyPressEvent(self, event):
        keycode = event.key()
        if 0 <= keycode <= 255:
            self.label.setText(f'Key pressed: {event.text()}, id: {keycode}')
        else:
            self.label.setText(f'Key pressed: {event.text()}')

    def mousePressEvent(self, event):
        mousecode = str(event.button())
        self.label.setText(f"Pressed the {(mousecode.split('.', 1)[1]).split('Button', 1)[0]} mouse button")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




