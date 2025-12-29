# # import sys
# # from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox



# # app = QApplication(sys.argv)

# # window = QWidget()
# # window.setWindowTitle("First window!")
# # # window.resize(400, 300)
# # window.setFixedSize(400, 300)
# # window.show()



# # sys.exit(app.exec())



# from os import name
# import sys
# from PyQt6.QtWidgets import (
#     QApplication, 
#     QWidget, 
#     QPushButton, 
#     QLabel,
#     QLineEdit, 
#     QVBoxLayout
# )

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
    
#         self.setWindowTitle("PQt6 Lesson 3")
#         self.setGeometry(300, 200, 400, 250)

#         self.label = QLabel("Enter something: ")
#         self.input_name = QLineEdit()
#         self.input_name.setPlaceholderText("Name ")
#         self.button = QPushButton("Greet")
#         self.button.clicked.connect(self.say_hello)
    

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.input_name)
#         layout.addWidget(self.button)       

#         self.setLayout(layout)

#     def say_hello(self):
#         name = self.input_name.text()
#         if name:
#             self.label.setText(f"Hello, {name}!")
#         else:
#             self.label.setText("Please enter your name.")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()

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
    QGridLayout,
    QLineEdit, 
    QVBoxLayout
)
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🧮 Calculator")
        self.setFixedSize(300, 400)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("""
            font-size: 26px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 10px;
        """)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0)
        ]
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 50)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    border-radius: 8px;
                    background-color: red;
                    color: white;
                }
            """)
            button.clicked.connect(self.on_button_click)

            if text == "C":
                grid.addWidget(button, row, col, 1, 4)
            else:
                grid.addWidget(button, row, col)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()
        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()