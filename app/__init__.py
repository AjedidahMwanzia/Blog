from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config_options




app=Flask(__name__)

app.config['SECRET_KEY']= 'secret'
db =SQLAlchemy(app)  

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



   

  