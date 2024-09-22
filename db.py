import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Stat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    value = db.Column(db.Integer)

    def __init__(self,name,value):
        self.name = name
        self.value = value 

    def as_dict (self):
       return {c.name: getattr(self,c.name) for c in self.__table__.columns}

class Health(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ##location = db.Column(db.text)
    hp = db.Column(db.Integer)

    def __init__(self,hp):
        self.hp = hp

    def as_dict (self):
       return {c.name: getattr(self,c.name) for c in self.__table__.columns}

class Armor(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Text)
    hp = db.Column(db.Integer)

    def __init__(self,location,hp):
        self.location = location
        self.hp = hp

    def as_dict (self): 
       return {c.name: getattr(self,c.name) for c in self.__table__.columns}
