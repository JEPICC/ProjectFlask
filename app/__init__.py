from flask import Flask, session
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from _datetime import timedelta


app = Flask(__name__)
mail = Mail()
bootstrap = Bootstrap()

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()

from .models import User, Task
from .views import page
from .api import api


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

def create_app(config):
    app.config.from_object(config)
    
    mail.init_app(app)
    csrf.init_app(app)
    if not app.config.get('TEST', False):# condicioanl para pruebas
        bootstrap.init_app(app)

    app.app_context().push()
    login_manager.init_app(app)
    #Configuracion para redirigir los accesos restringidos
    login_manager.login_view = '.login'
    login_manager.login_message = 'Por favor inicia session'
    login_manager.refresh_view = 'relogin'
    login_manager.needs_refresh_message = (u"Session timedout, please re-login")
    login_manager.needs_refresh_message_category = "info"
    
    app.register_blueprint(page)

    app.register_blueprint(api)

    #Inicializacion de Tabla
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app