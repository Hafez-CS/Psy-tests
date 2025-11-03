import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="tas_results.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tas_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT,
                    total_score INTEGER,
                    interpretation TEXT,
                    predicted_reaction TEXT,
                    test_date TEXT
                )
            """)
            conn.commit()

    def save_result(self, user_name, total_score, interpretation, predicted_reaction):
      
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tas_results (user_name, total_score, interpretation, predicted_reaction, test_date)
                VALUES (?, ?, ?, ?, ?)
            """, (user_name, total_score, interpretation, predicted_reaction, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

    def get_all_results(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tas_results")
            return cursor.fetchall()

    def get_user_history(self, user_name):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tas_results WHERE user_name = ?", (user_name,))
            return cursor.fetchall()