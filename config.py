import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:user@localhost/cores'
    SECRET_KEY='30011397'
    UPLOADED_PHOTOS_DEST = 'app/static/profiles'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
