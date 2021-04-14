from flask_seeder import Seeder, Faker, generator
from models import DailyReports

class DailyReportsSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=DailyReports,
            init={
                "title": generator.String('test|hoge'),
                "body_text": generator.String('みなさんこんにちは、今日もいい天気ですね')
            }
        )

        for post in faker.create(16):
            print("Adding post: {}".format(post))
            self.db.session.add(post)
