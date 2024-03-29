import os

class Config:
    '''
    General configuration parent class
    '''
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='123'


    '''
    mail configurations
    '''

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = "Blog"
    SENDER_EMAIL = os.environ.get("MAIL_USERNAME")




class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ian:vionashina@localhost/blog_test'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:vionashina@localhost/blog'

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

