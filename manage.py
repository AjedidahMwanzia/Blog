from app import create_app,db
from flask_script import Manager,Server
from app import models
from flask_migrate import Migrate, MigrateCommand
# Creating app instance
app = create_app('production')
app.config['SECRET_KEY'] = 'asldfkawo'

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://moringa:jay@localhost/blog'
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(testsg)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role, )

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'asldfkawo'
    manager.run()