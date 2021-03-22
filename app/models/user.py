from database import db
import json
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  email = db.Column(db.String(128), nullable = False, unique = True)
  name = db.Column(db.String(64), nullable = False)
  password = db.Column(db.String(128), nullable = False)
  
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email
    }
  
  def to_json(self):
    return json.dumps(self.to_dict())
