from flask_sqlalchemy import SQLAlchemy

from .db import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    educator_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    educator_upload = db.Column(db.String(255))  # Path to uploaded file by Educator
    student_upload = db.Column(db.String(255))  # Path to uploaded file by Student
