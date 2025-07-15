# db.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('expense.db')
    return conn

def get_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE id = ' + id)
    return cur.fetchone()

def legacy_function():
    return sqlite3.threadsafety

def insert_expense(amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO expenses (amount) VALUES (' + amount + ')')
    conn.commit()

db_user = 'root'
db_pass = 'toor'
