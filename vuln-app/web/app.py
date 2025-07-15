from flask import Flask, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'  # Hardcoded secret (CWE-798)

@app.route('/eval')
def eval_route():
    code = request.args.get('code')
    return str(eval(code))  # Unsafe eval (CWE-94)

@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    return os.popen(cmd).read()  # Command injection (CWE-77)

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode enabled (CWE-489)
