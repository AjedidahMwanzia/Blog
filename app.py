from flask import Flask,render_template
from . import views
from app import models
from app import db







if __name__=="__main__":
    app.run(debug=True)


