from datetime import datetime

from database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class DailyReports(db.Model):
    __tablename__ = 'daily_reports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(UUID(as_uuid=True), primary_key=True,
                     default=uuid.uuid4, unique=True)
    title = db.Column(db.Text, nullable=False)
    body_text = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, body_text):
        self.title = title
        self.body_text = body_text
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at


    def to_dict(self):
        return {
            'id': self.id,
            'uuid': str(self.uuid),
            'title': self.title,
            'body_text': self.body_text,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
