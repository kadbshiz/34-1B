import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QSpinBox, QComboBox, QCheckBox, QListWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моя библиотека")
        self.setGeometry(200, 200, 800, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название")
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Автор")
        self.year_input = QSpinBox()
        self.year_input.setRange(1400, 2025)
        self.year_input.setValue(2025)
        self.genre_input = QComboBox()
        self.genre_input.addItems(["Роман", "Детектив", "Фантастика", "Фэнтези", "Мистика"])
        self.read_input = QCheckBox("Прочитано")
        self.read_input.setChecked(False)

        btn_add = QPushButton("Добавить")
        btn_add.clicked.connect(self.add_book)
        btn_clear = QPushButton("Очистить")
        btn_clear.clicked.connect(self.clear_form)
        btn_exit = QPushButton("Выход")
        btn_exit.clicked.connect(self.close)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Название:"))
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(QLabel("Автор:"))
        form_layout.addWidget(self.author_input)
        form_layout.addWidget(QLabel("Год:"))
        form_layout.addWidget(self.year_input)
        form_layout.addWidget(QLabel("Жанр:"))
        form_layout.addWidget(self.genre_input)
        form_layout.addWidget(self.read_input)
        form_layout.addSpacing(20)
        form_layout.addWidget(btn_add)
        form_layout.addWidget(btn_clear)
        form_layout.addWidget(btn_exit)
        form_layout.addStretch()

        self.list_widget = QListWidget()
        self.list_widget.addItem("Название | Автор | Год | Жанр | Прочитано")

        main_layout = QHBoxLayout()
        main_layout.addLayout(form_layout, 2)
        main_layout.addWidget(self.list_widget, 5)

        central_widget.setLayout(main_layout)
        self.status = self.statusBar()

    def add_book(self):
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        if not title or not author:
            QMessageBox.warning(self, "Ошибка", "Введите название и автора!")
            return
        year = str(self.year_input.value())
        genre = self.genre_input.currentText()
        read = "Да" if self.read_input.isChecked() else "Нет"
        item_text = f"{title} | {author} | {year} | {genre} | {read}"
        self.list_widget.addItem(item_text)
        self.status.showMessage(f"Добавлена книга: {title}", 5000)

    def clear_form(self):
        self.title_input.clear()
        self.author_input.clear()
        self.year_input.setValue(2025)
        self.genre_input.setCurrentIndex(0)
        self.read_input.setChecked(False)
        self.status.showMessage("Форма очищена", 3000)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

