from enum import unique
from time import timezone
from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Alerts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Alerts_text = db.Column(db.String(10000))
    #Alerts_image = 
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    alerts = db.relationship('Alerts')

