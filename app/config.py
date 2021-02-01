import os
basedir = os.path.abspath(os.path.dirname('__file__'))

class Config:
    ENV='production'
    DEBUG=False
    TESTING=False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV='development'
    # SERVER_NAME="0.0.0.0"
    DEBUG = True
    

class TestingConfig(Config):
    ENV='testing'
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
    }