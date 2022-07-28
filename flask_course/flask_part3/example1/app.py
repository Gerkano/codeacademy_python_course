import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=True, nullable=False) 
    address = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=False)
    
# prie konstruktoriaus irgi nepamirštame pridėti:
    def __init__(self, name, email, message, phone, address):
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f'{self.name} - {self.email}'