import os

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': os.getenv('RDS_USERNAME'),
    'password': os.getenv('POSTGRES_PASSWORD', 'develop'),
    'host': '{}:5432'.format(str(os.getenv('RDS_HOSTNAME'))),
    'name': 'postgres'
})
