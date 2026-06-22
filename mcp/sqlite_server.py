import sqlite3

def init_db():
    conn = sqlite3.connect("enterprise.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        response TEXT
    )
    """)

    conn.commit()
    conn.close()

def log_interaction(query, response):
    conn = sqlite3.connect("enterprise.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (query, response) VALUES (?, ?)",
        (query, response)
    )

    conn.commit()
    conn.close()