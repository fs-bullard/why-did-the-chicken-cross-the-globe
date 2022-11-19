from flask import Blueprint
from flask import Flask
from flask import request, render_template, session

from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

