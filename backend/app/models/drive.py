from flask_sqlalchemy import SQLAlchemy

from .db import db

class Drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.relationship('Note', backref='drive', lazy=True)
    resources = db.relationship('Resource', backref='drive', lazy=True)
    
<<<<<<< HEAD
=======

>>>>>>> 7050c94 ( Added Authentication, Fixed template error, Updated Templates)
