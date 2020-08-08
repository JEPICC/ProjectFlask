from app import create_app, db, User, Task

from config import config

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


#configurado para entorno de desarrollo
app = create_app(config['development'])
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)

if __name__ == "__main__":
    manager = Manager(app)
    
    #Shell para trabajar los modelos como objetos en tiempo de ejecucion
    manager.add_command('shell', Shell(make_context=make_shell_context))
    
    #Crea comando para migrar BBDD
    manager.add_command('db', MigrateCommand)
    
    #pruebas unitarias
    @manager.command
    def test():
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner().run(tests)
        
    manager.run()