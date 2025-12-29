import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Homework")
        self.setFixedSize(300, 200)

        self.label = QLabel("Введите текст")
        self.line = QLineEdit()

        self.button_show = QPushButton("Показать")
        self.button_exit = QPushButton("Выход")

        self.button_show.clicked.connect(self.show_text)
        self.button_exit.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        layout.addWidget(self.button_show)
        layout.addWidget(self.button_exit)

        self.setLayout(layout)

    def show_text(self):
        self.label.setText(self.line.text())


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())
