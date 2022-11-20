from flask import Blueprint
from flask import Flask
from flask import request, render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User
from . import db
from .get_recipes import get_recipes, get_recipe_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', name=current_user.name)

@main.route('/info')
def info():
    return render_template('info.html', title='Info')

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
    if ',' in ingredients:
        ingredients = ingredients.split(',')
    else:
        ingredients = [ingredients]

    recipes = get_recipes(ingredients)
    recipes_data = get_recipe_data(recipes)
    # print(recipes_data)
    return render_template('recipes.html', title='Recipes', recipes=recipes_data, n=len(recipes))

@main.route('/choice')
@login_required
def recipe_choice():
    recipe_key = request.form.get('recipe')
    print(recipe_key)
    recipe = get_recipe_data([recipe_key])
    print(recipe)
    return render_template('chosen_recipe.html', recipe=recipe)

@main.route('/chicken')
@login_required
def chicken():
    return render_template('chicken.html', title='Recipes')

@main.route('/bake')
@login_required
def bake():
    key = 'Chicken pasta bake'
    recipe = get_recipe_data([key])
    graph_url = "https://chart-studio.plotly.com/~YMTran/2.embed"

    return render_template('chosen_recipe.html', recipe=recipe, key=key, graph=graph_url)

@main.route('/ragu')
@login_required
def ragu():
    key = 'Chicken & chorizo ragu'
    recipe = get_recipe_data([key])
    graph_url = "https://chart-studio.plotly.com/~YMTran/2.embed"

    return render_template('chosen_recipe.html', recipe=recipe, key=key, graph=graph_url )

@main.route('/mustard')
@login_required
def mustard():
    key = "Mustard & parmesan- crumbed chicken"
    recipe = get_recipe_data([key])
    graph_url = "https://chart-studio.plotly.com/~YMTran/2.embed"
    return render_template('chosen_recipe.html', recipe=recipe, key=key, graph=graph_url )

@main.route('/roast')
@login_required
def roast():
    key = "Roast chicken with squashed new potatoes & cheesy creamed spinach"
    recipe = get_recipe_data([key])
    graph_url = "https://chart-studio.plotly.com/~YMTran/17.embed"

    return render_template('chosen_recipe.html', recipe=recipe, key=key, graph=graph_url)


