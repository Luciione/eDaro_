from flask_sqlalchemy import SQLAlchemy

from .db import db

class Educator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    assessments = db.relationship('Assessment', backref='educator', lazy=True)
    classes = db.relationship('Class', backref='educator', lazy=True)
    resources = db.relationship('Resource', backref='educator', lazy=True)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'))
    drive = db.relationship('Drive', backref='educator', uselist=False)
    

