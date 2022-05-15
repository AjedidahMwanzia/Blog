from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config_options


db =SQLAlchemy()
def create_app(config_name):
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:jay@localhost/blog'
    app.config['SECRET_KEY']= 'secret'

 

    db.init_app(app)
    from . import views,form

    return app