from flask import Blueprint
from flask import Flask
from flask import request, render_template, session
from flask_bootstrap import Bootstrap5
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', title='Home')

@auth.route('/signup')
def signup():
    return render_template('signup.html', title='Home')

@auth.route('/logout')
def logout():
    return 'Logout'