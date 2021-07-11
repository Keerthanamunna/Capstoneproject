import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json



database_host = os.getenv('database_host', '127.0.0.1:5432')  
database_username = os.getenv('database_username', 'postgres')  
database_name = os.getenv('database_name', 'TravelDiaries')
database_path = 'postgresql+psycopg2://{}@{}/{}'.format(database_username, database_host, database_name)

db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Venue

'''
class Venue(db.Model):  
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  vname = db.Column(db.String) 
  description = db.Column(db.String)
  places = db.relationship('Place', backref='venues') 
  #difficulty = Column(Integer)

  def __init__(self, vname, description):
    self.vname = vname
    self.description = description

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
      'vname': self.vname,
      'description': self.description,
      'places': self.places
      
    }

'''
Place

'''
class Place(db.Model):  
  __tablename__ = 'places'

  id = db.Column(db.Integer, primary_key=True)
  pname = db.Column(db.String)
  pdescription = db.Column(db.String)
  #pimage = db.Column(db.bytea)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

  def __init__(self, pname, pdescription):
    self.pname = pname
    self.pdescription = pdescription
    
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
      'pname': self.pname,
      'pdescription': self.pdescription,
      'venue_id' : self.venue_id
    }
    