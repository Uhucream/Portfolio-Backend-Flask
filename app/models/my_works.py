from database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class MyWorks(db.Model):
    __tablename__ = 'my_works'

    id = db.Column(db.Integer, unique=True)
    uuid = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True)
    name = db.Column(db.Text, nullable=False)
    endpoint_uri = db.Column(db.Text, nullable=False, unique=True)
    top_page_outline = db.Column(db.Text, nullable=False)
    work_url = db.Column(db.Text, nullable=True)
    work_picture_url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, endpoint_uri, top_page_outline, **args):
        try:
            self.id = args['id']
        except KeyError:
            self.id = None

        self.name = name
        self.endpoint_uri = endpoint_uri
        self.top_page_outline = top_page_outline

        try:
            self.description = args['description']
        except KeyError:
            self.description = None

        try:
            self.work_url = args['work_url']
        except KeyError:
            self.work_url = None

        try:
            self.work_picture_url = args['work_picture_url']
        except KeyError:
            self.work_picture_url = None


    def to_dict(self):
        return {
            'id': self.id,
            'uuid': str(self.uuid),
            'name': self.name,
            'endpoint_uri': self.endpoint_uri,
            'top_page_outline': self.top_page_outline,
            'description': self.description,
            'work_url': self.work_url,
            'work_picture_url': self.work_picture_url,
        }
