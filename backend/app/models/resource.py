from flask_sqlalchemy import SQLAlchemy

from .db import db

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    educator_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    document = db.Column(db.String(255))  # Path to uploaded file
    instructions = db.Column(db.Text)
    

