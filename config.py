import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    debug = True

    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
