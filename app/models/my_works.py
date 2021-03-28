from database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class MyWorks(db.Model):
    __tablename__ = 'my_works'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True)
    name = db.Column(db.Text, nullable=False)
    endpoint_uri = db.Column(db.Text, nullable=False, unique=True)
    top_page_outline = db.Column(db.Text, nullable=False)
    work_url = db.Column(db.Text, nullable=True)
    work_picture_url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, endpoint_uri, top_page_outline, work_url, work_picture_url, description):
        self.name = name
        self.endpoint_uri = endpoint_uri
        self.top_page_outline = top_page_outline
        self.description = description
        self.work_url = work_url
        self.work_picture_url = work_picture_url

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'endpoint_uri': self.endpoint_uri,
            'top_page_outline': self.top_page_outline,
            'description': self.description,
            'work_url': self.work_url,
            'work_picture_url': self.work_picture_url,
        }
