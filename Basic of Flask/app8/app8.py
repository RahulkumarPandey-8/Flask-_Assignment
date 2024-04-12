from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app8 = Flask(__name__)

@app8.route('/')
def home():
    return render_template('index.html')


@app8.route('/login')
def login():
    return render_template('login.html')


@app8.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app8.run(debug=True)
