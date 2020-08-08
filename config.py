class Config:
    SECRET_KEY = 'SelFY2zKa4PfuLVoi1tyrJJILp7VV5EJ'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@189.156.123.95:3306/proyect_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jepicco@gmail.com'
    MAIL_PASSWORD = 'passwoer'

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@189.156.123.95:3306/proyect_flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development' : DevelopmentConfig,
    'default' : DevelopmentConfig,
    'test' : TestConfig
}