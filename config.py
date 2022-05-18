import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):


    DEBUG = True

class DevConfig(Config):
    pass


config_options = {
'development':DevConfig,
'production':ProdConfig
}