from flask import Blueprint, request, redirect, render_template_string
import sqlite3

bp = Blueprint('routes', __name__)

@bp.route('/user')
def user():
    user = request.args.get('user')
    conn = sqlite3.connect('expense.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE name = '{user}'")  # SQL injection (CWE-89)
    return str(cur.fetchall())

@bp.route('/xss')
def xss():
    input = request.args.get('input')
    return render_template_string(f'<h1>{input}</h1>')  # XSS (CWE-79)

@bp.route('/redirect')
def open_redirect():
    url = request.args.get('url')
    return redirect(url)  # Open redirect (CWE-601)

@bp.route('/error')
def error():
    1/0  # Unhandled exception (CWE-755)
