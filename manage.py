
from app.models import Users
from app import db


app.config['SECRET_KEY']= 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'



    
if __name__ == '__main__':
    manager.run()





