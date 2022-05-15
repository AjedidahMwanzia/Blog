from flask import Flask,render_template
from app import views
from app.models import Users
from app import db,create_app



@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()





