from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config_options


db =SQLAlchemy()
def create_app(config_name):
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:jay@localhost/test1'
    app.config['SECRET_KEY']= 'secret'

    app.config.from_object(config_options[config_name])
       # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    db.init_app(app)
    db.create_all(app=app)	
    from . import views,form

    return app