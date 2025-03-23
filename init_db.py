import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task TEXT NOT NULL,
    user_answer TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

connection.commit()
connection.close()

print("База данных и таблица users успешно созданы.")
