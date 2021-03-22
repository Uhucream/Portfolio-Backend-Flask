from database import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BlockedTokens(db.Model):
  __tablename__ = 'blocked_tokens'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  jti = db.Column(db.String(36), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  
  def __init__(self, jti):
    self.jti = jti
