# import sqlite3

# con = sqlite3.connect("database.db")
# cur = con.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS zebras(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# age INTEGER NOT NULL
# )""")

# cur.execute("INSERT INTO zebras (name, age) VALUES (?, ?)", ("Marty", 10))
# con.commit()

# cur.execute("SELECT * FROM zebras")
# for row in cur.fetchall():
#     print(row)

# con.close()

import sys
from PyQt6.QtWidgets import(
     QApplication,
     QWidget, 
     QPushButton, 
     QVBoxLayout, 
     QLineEdit,
     Qlabel)

class SQLApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTirtle("Lesson 4 - SQL + pyQt6")
        self.setGeometry(300, 200, 300, 250)
        
        self.label = Qlabel("Enter something", self)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter the name")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.result = Qlabel()
        
        self.age_input = QLineEdit(self)
        self.age_input.setPlaceholderText("Enter zebra age")
        self.layout.addWidget(self.age_input)
        
        self.add_button = QPushButton("Add Zebra", self)
        self.add_button.clicked.connect(self.add_zebra)
        self.layout.addWidget(self.add_button)
        
        self.setLayout(self.layout)
    
    def add_zebra(self):
        name = self.name_input.text()
        age = self.age_input.text()
        print(f"Zebra added: Name={name}, Age={age}")
        # Here you would add the code to insert into the database