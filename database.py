import sqlite3
import datetime

class Database:
    def __init__(self, db_file='expenses.db', initial_balance=0):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table(initial_balance)

    def create_table(self, initial_balance):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT,
                Category TEXT,
                Amount REAL,
                Description TEXT,
                Balance REAL,
                Type TEXT DEFAULT 'expense'
            )
        ''')

        # Check if table is empty
        self.cursor.execute("SELECT COUNT(*) FROM expenses")
        row_count = self.cursor.fetchone()[0]

        if row_count == 0:
            self.cursor.execute("INSERT INTO expenses (Date, Category, Amount, Balance, Type) VALUES (?, ?, ?, ?, ?)",
                                 (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Initial Balance', initial_balance, initial_balance, 'initial'))

        self.conn.commit()

    def add_transaction(self, category, amount, description='', transaction_type=None):
        if transaction_type is None:
            transaction_type = 'income' if amount >= 0 else 'expense'

        self.cursor.execute("SELECT Balance FROM expenses ORDER BY ID DESC LIMIT 1")
        last_balance = self.cursor.fetchone()[0]
        new_balance = last_balance + amount

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO expenses (Date, Category, Amount, Description, Balance, Type) VALUES (?, ?, ?, ?, ?, ?)",
                           (date, category, amount, description, new_balance, transaction_type))
        self.conn.commit()

    def get_current_balance(self):
        self.cursor.execute("SELECT Balance FROM expenses ORDER BY ID DESC LIMIT 1")
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def close(self):
        self.conn.close()

# Create an instance of the database
db = Database()
