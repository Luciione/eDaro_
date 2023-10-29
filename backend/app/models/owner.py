from flask_sqlalchemy import SQLAlchemy

from .db import db

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    schools = db.relationship('School', backref='owner', lazy=True)
    

