try:
    from local_config import Config as K
except ImportError:
    pass




class Config(object):
    SECRET_KEY = K.SECRET_KEY or "some_key"
    SQLALCHEMY_DATABASE_URI = K.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
