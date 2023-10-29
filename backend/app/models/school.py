from flask_sqlalchemy import SQLAlchemy

from .db import db

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    classes = db.relationship('Class', backref='school', lazy=True)
    

