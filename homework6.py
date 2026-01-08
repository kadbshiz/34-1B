import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
    QLabel,
    QTableWidget,
    QSpinBox,
    QComboBox,
    QCheckBox,
    QStatusBar,
    QTableWidgetItem
)
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        read INTEGER
    )
""")
conn.commit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моя библиотека")
        self.setGeometry(200, 250, 800, 500)

        central = QWidget()
        self.setCentralWidget(central)
        self.layout = QGridLayout()
        central.setLayout(self.layout)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название")

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Автор")

        self.year_input = QSpinBox()
        self.year_input.setRange(1400, 2025)
        self.year_input.setValue(2023)

        self.genre_input = QComboBox()
        self.genre_input.addItems(["Роман", "Детектив", "Фантастика"])

        self.read_checkbox = QCheckBox("Прочитано")

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_book)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear_form)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Название", "Автор", "Год", "Жанр", "Прочитано"])
        self.table.setSortingEnabled(True)

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(self.author_input)
        form_layout.addWidget(self.year_input)
        form_layout.addWidget(self.genre_input)
        form_layout.addWidget(self.read_checkbox)
        form_layout.addWidget(self.add_button)
        form_layout.addWidget(self.clear_button)
        form_layout.addWidget(self.exit_button)

        self.layout.addLayout(form_layout, 0, 0)
        self.layout.addWidget(self.table, 0, 1)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)  # use native status bar
        self.status_bar.showMessage("Готово", 2000)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()

        if not title or not author:
            QMessageBox.warning(self, "Ошибка", "Введите название и автора!")
            return
        year = self.year_input.value()
        genre = self.genre_input.currentText()
        read = 1 if self.read_checkbox.isChecked() else 0
        cursor.execute("""
            INSERT INTO books (title, author, year, genre, read)
            VALUES (?, ?, ?, ?, ?)
        """, (title, author, year, genre, read))
        conn.commit()

        self.load_books()
        self.status_bar.showMessage(f"Добавлена книга: {title}", 5000)
        self.status_bar.repaint()

    def clear_form(self):
        self.title_input.clear()
        self.author_input.clear()
        self.year_input.setValue(2023)
        self.genre_input.setCurrentIndex(0)
        self.read_checkbox.setChecked(False)
        self.status_bar.showMessage("Форма очищена", 3000)
        self.status_bar.repaint()

    def load_books(self):
        self.table.setRowCount(0)
        cursor.execute("SELECT title, author, year, genre, read FROM books")

        for row_data in cursor.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                if column_number == 4:
                    data = "Да" if data == 1 else "Нет"
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.load_books()
sys.exit(app.exec())
