import os

if os.getenv('RDS_HOSTNAME') is not None:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(**{
        'user': os.getenv('RDS_USERNAME'),
        'password': os.getenv('RDS_PASSWORD'),
        'host': str(os.getenv('RDS_HOSTNAME')),
        'port': str(str(os.getenv('RDS_PORT'))),
        'name': os.getenv('RDS_DB_NAME')
    })
else:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
