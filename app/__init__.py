from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config_options


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY']= 'secret'

db =SQLAlchemy(app)

# db.init_app(app)
from . import views,form