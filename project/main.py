from flask import Blueprint
from flask import Flask
from flask import request, render_template, session
from flask_login import login_required, current_user

from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', name=current_user.name)

