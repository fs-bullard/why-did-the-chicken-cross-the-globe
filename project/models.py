from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    carbon_totals = db.relationship('Carbon_Total', backref='user', lazy=True)

class Carbon_Total(UserMixin, db.model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    value = db.Column(db.Integer)