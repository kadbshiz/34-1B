# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox



# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("First window!")
# # window.resize(400, 300)
# window.setFixedSize(400, 300)
# window.show()



# sys.exit(app.exec())














import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QLabel,
    QLineEdit, 
    QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My second lesson!")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter something:")
        self.input = QLineEdit()
        self.button = QPushButton("Show")
        self.result = QLabel("")

        self.button.clicked.connect(self.show_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def show_text(self):
        text = self.input.text()
        self.label.setText(f"You entered: {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()