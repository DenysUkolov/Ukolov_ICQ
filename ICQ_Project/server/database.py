import sqlite3

def init_db():
    conn = sqlite3.connect('database/messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message(message):
    conn = sqlite3.connect('database/messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (sender, message) VALUES (?, ?)
    ''', message.split(": ", 1))
    conn.commit()
    conn.close()
