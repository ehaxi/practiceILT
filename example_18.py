import sys
from PyQt6.QtGui import QMouseEvent, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.red, 3)
        painter.setPen(pen)
        painter.drawLine(10, 10, self.rect().width() - 10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




