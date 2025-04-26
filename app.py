# Vulnerable Flask App for SonarCloud SAST Testing

from flask import Flask, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Hardcoded database path
DB_PATH = "test.db"

# Hardcoded secret key (bad practice)
app.secret_key = "supersecretkey123"

@app.route('/')
def home():
    return "Welcome to the vulnerable app!"

@app.route('/unsafe_eval', methods=['POST'])
def unsafe_eval():
    data = request.form.get('code')
    eval(data)  # Code Injection vulnerability
    return "Evaluated."

@app.route('/unsafe_sql', methods=['GET'])
def unsafe_sql():
    user_id = request.args.get('id')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # SQL Injection vulnerability
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    data = cursor.fetchall()
    conn.close()
    return str(data)

@app.route('/unsafe_command', methods=['GET'])
def unsafe_command():
    cmd = request.args.get('cmd')
    os.system(cmd)  # Command Injection vulnerability
    return "Command executed."

@app.route('/open_redirect', methods=['GET'])
def open_redirect():
    url = request.args.get('url')
    return redirect(url)  # Open Redirect vulnerability

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
