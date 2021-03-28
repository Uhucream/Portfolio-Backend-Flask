from database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class MyWorks(db.Model):
    __tablename__ = 'my_works'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    work_name = db.Column(db.Text, nullable=False)
    work_picture_url = db.Column(db.Text, nullable=True)
    work_url = db.Column(db.Text, nullable=True)
    work_description = db.Column(db.Text, nullable=True)

    def __init__(self, work_name, work_url, work_picture_url, work_description):
        self.work_name = work_name
        self.work_description = work_description
        self.work_url = work_url
        self.work_picture_url = work_picture_url

    def to_dict(self):
        return {
            'id': str(self.id),
            'work_name': self.work_name,
            'work_description': self.work_description,
            'work_url': self.work_url,
            'work_picture_url': self.work_picture_url,
        }
