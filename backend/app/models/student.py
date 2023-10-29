from flask_sqlalchemy import SQLAlchemy

from .db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    assessments = db.relationship('Assessment', backref='student', lazy=True)
    classes = db.relationship('Class', backref='student', lazy=True)
    notes = db.relationship('Note', backref='student', lazy=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'))
    drive = db.relationship('Drive', backref='student', uselist=False)
    

