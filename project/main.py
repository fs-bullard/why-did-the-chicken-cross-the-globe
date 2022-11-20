from flask import Blueprint
from flask import Flask
from flask import request, render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User
from . import db
import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', name=current_user.name)

@main.route('/addlist')
def add_list():
    # If user isn't logged in, make them
    if not current_user.is_authenticated:
        flash('Please log in to add a new shopping list')
        return redirect(url_for('auth.login'))
    return render_template('new_list.html', title='New List')

@main.route('/recipes', methods=['POST'])
@login_required
def recipes():
    ingredients = request.form.get('shopping_list')
    print(ingredients)

    

    return render_template('recipes.html', title='Recipes')


