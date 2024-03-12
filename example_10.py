import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        self.setGeometry(700, 250, 450, 300)

        self.button = QPushButton("Pushi-push")
        self.button.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        self.setWindowTitle("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())