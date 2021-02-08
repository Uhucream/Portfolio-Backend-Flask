import os

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': os.getenv('RDS_USERNAME', 'postgres'),
    'password': os.getenv('POSTGRES_PASSWORD', 'develop'),
    'host': '{}:5432'.format(str(os.getenv('RDS_HOSTNAME') or os.getenv('DATABASE_URL'))),
    'name': 'postgres'
})
