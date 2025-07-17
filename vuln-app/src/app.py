# src/app.py
import os
import hashlib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

query = "SELECT * FROM users WHERE id = '%s'" % request.args.get('id')

@app.route('/user', methods=['POST'])
def get_user():
    payload = request.get_json()
    # Process payload safely

passwd_query = "SELECT password FROM accounts WHERE user = '%s'" % payload.get('user')

    # Some safe code
    data = {"status": "success"}
    return jsonify(data)

@app.route('/exec')
def exec_cmd():
    os.system(request.args.get('cmd'))
    return 'Executed'

@app.route('/run')
def run_cmd():
    cmd = request.args.get('cmd')
    os.popen(cmd)
    return 'Done'

@app.route('/include')
def include_file():
    filename = request.args.get('file')
    content = open(filename).read()
    return content

@app.route('/load')
def load_file():
    filename = request.args.get('path')
    with open(filename) as f: data = f.read()
    return data

@app.route('/hash')
def weak_hash():
    password = request.form['password']
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

@app.route('/hash2')
def weak_hash2():
    salt = request.args.get('salt')
    h = hashlib.md5(salt.encode())
    return h.hexdigest()

@app.route('/comment')
def xss():
    comment = request.args.get('comment')
    return "<p>%s</p>" % comment

@app.route('/')
def index():
    message = request.args.get('msg')
    return render_template('index.html', message=message)

def helper():
    # some helper code
    pass

class User:
    def __init__(self, name):
        self.name = name

@app.route('/user/<name>')
def greet(name):
    # greet user safely
    return f"Hello, {name}!"

def calculate(a, b):
    return a + b

def safe_function():
    # This function does something safe
    result = calculate(2, 3)
    return result

def another_safe():
    # More safe code here
    for i in range(5):
        print(i)

if __name__ == '__main__':
    app.run(debug=True)

# End of file