import sqlite3

def connect_db():
    conn = sqlite3.connect('expense.db')  # No error handling (CWE-252)
    return conn

def get_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE id = ' + id)  # SQL injection (CWE-89)
    return cur.fetchone()

def legacy_function():
    # Deprecated usage (CWE-676)
    return sqlite3.threadsafety

def insert_expense(amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO expenses (amount) VALUES (' + amount + ')')  # SQL injection (CWE-89)
    conn.commit()

# Hardcoded DB credentials (CWE-798)
db_user = 'root'
db_pass = 'toor'
