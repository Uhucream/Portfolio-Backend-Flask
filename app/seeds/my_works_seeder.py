from flask_seeder import Seeder, Faker, generator
from models import MyWorks
import uuid

class MyWorksSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=MyWorks,
            init={
                "name": generator.String('test work'),
                "endpoint_uri": generator.String('test_work{}'.format(uuid.uuid4)),
                "top_page_ourline": generator.String('hoge'),
                "work_url": generator.IPv4(),
                "work_picture_url": generator.IPv4(),
                "work_picture_thumbnail_url": generator.IPv4(),
                "description": generator.String("hoge")
            }
        )

        for work in faker.create(16):
            print("Adding a work: {}".format(work))
            self.db.session.add(work)
