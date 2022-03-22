from datetime import date
import os
from click import DateTime
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movie
Have title and release date
'''
class Movies(db.Model):  
    __tablename__ = 'movies'

    id = Column(db.Integer, primary_key=True)
    title = Column(String, unique=True)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date}


'''
Actor
Have name, age and gender
'''
class Actors(db.Model):  
    __tablename__ = 'actors'

    id = Column(db.Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(db.Integer)
    gender = Column(String, unique=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender}