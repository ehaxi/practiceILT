import sys
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    class CustomButton(QPushButton):
        def __init__(self, text):
            super().__init__(text=text)
            super().setCheckable(False)

        def mouseReleaseEvent(self, event):
            super().mouseReleaseEvent(event)
            event.ignore()

    def __init__(self):
        super().__init__()
        self.button = self.CustomButton("Try to press")
        self.button.released.connect(self.button_released)
        self.setCentralWidget(self.button)

    def mouseReleaseEvent(self, event):
        print(f"released {event}")
        event.ignore()
    def button_released(self):
        print(f"Button pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




