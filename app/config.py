import os
from database.postgresql import SQLALCHEMY_DATABASE_URI as DATABASE_URI
basedir = os.path.abspath(os.path.dirname('__file__'))

class Config:
    ENV='production'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = str(os.urandom(24))
    SQLALCHEMY_ECHO = True
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_SAMESITE = 'LaX'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    JWT_COOKIE_SECURE = False
    ENV='development'
    DEBUG = True
    

class TestingConfig(Config):
    ENV='testing'
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
    }
