# app.py
from flask import Flask, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

@app.route('/eval')
def eval_route():
    code = request.args.get('code')
    return str(eval(code))

@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    return os.popen(cmd).read()

if __name__ == '__main__':
    app.run(debug=True)
