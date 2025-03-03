import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from database import InsertInTableUsers, hash_password

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        birth_date = request.form['birth_date']
        email = request.form['email']
        password = request.form['password']

        if len(password) < 6 or len(password) > 12:
            print('La contraseña debe tener entre 6 y 12 caracteres.', 'error')
            return redirect(url_for('register'))

        hashed_password = hash_password(password)

        if InsertInTableUsers((username, hashed_password.decode('utf-8'), birth_date, email)):
            print('registered u ser', 'success')
        else:
            print('Error to register', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

