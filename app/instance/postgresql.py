import os

if os.getenv('FLASK_CONFIG') == 'development':
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
        'user': os.getenv('RDS_USERNAME', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD', 'develop'),
        'host': '{}:5432'.format(str(os.getenv('RDS_HOSTNAME'))),
        'name': 'postgres'
    })
else:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
