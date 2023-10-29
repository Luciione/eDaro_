from flask_sqlalchemy import SQLAlchemy

from .db import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    educator_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    

