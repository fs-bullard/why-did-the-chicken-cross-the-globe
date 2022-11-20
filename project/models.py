from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # shopping_lists = db.relationship('Shopping_List', backref='user', lazy=True)
    carbon_totals = db.relationship('Carbon_Total', backref='user', lazy=True)

# class Shopping_List(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date, nullable=False)
#     ingredients = db.relationship('Ingredient', backref='shopping_list', lazy=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class Ingredient(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_list.id'), nullable=False)

class Carbon_Total(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


